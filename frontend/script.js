const form = document.getElementById('email-form');
const textInput = document.getElementById('email-text');
const fileInput = document.getElementById('email-file');
const submitButton = document.getElementById('submit-button');
const loadingIndicator = document.getElementById('loading-indicator');
const resultArea = document.getElementById('result-area');
const resultCategory = document.getElementById('result-category');
const resultResponse = document.getElementById('result-response');
const copyButton = document.getElementById('copy-button');
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;
const historySection = document.getElementById('history-section');
const historyList = document.getElementById('history-list');
const historyEmptyMessage = document.getElementById('history-empty-message');
const MAX_HISTORY_ITEMS = 5; 


function applyTheme(theme) {
    if (theme === 'dark') {
        body.classList.add('dark-mode');
        themeToggle.checked = true;
    } else {
        body.classList.remove('dark-mode');
        themeToggle.checked = false;
    }
}

const savedTheme = localStorage.getItem('theme') || 'light';
applyTheme(savedTheme);

themeToggle.addEventListener('change', () => {
    const newTheme = themeToggle.checked ? 'dark' : 'light';
    localStorage.setItem('theme', newTheme);
    applyTheme(newTheme);
});



form.addEventListener('submit', async (event) => {
    event.preventDefault(); 

    const text = textInput.value;
    const file = fileInput.files[0];

    if (!text && !file) {
        alert('Por favor, cole um texto ou selecione um arquivo.');
        return;
    }

    if (text && file) {
        alert('Por favor, envie apenas texto ou um arquivo, não ambos.');
        return;
    }

    const formData = new FormData();
    if (text) {
        formData.append('email_text', text);
    } else if (file) {
        formData.append('email_file', file);
    }

    loadingIndicator.classList.remove('hidden');
    resultArea.classList.add('hidden');
    submitButton.disabled = true;

    try {
        const response = await fetch('http://localhost:8000/api/v1/classify-email', {
            method: 'POST',
            body: formData,
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || 'Ocorreu um erro na resposta da API.');
        }
        
        displayResults(data);

    } catch (error) {
        console.error("--- DETALHES COMPLETOS DO ERRO ---");
        console.error("Tipo de Erro:", error.name);     
        console.error("Mensagem:", error.message);    
        console.error("Objeto do Erro:", error);        
        console.error("---------------------------------");
        

        displayError(`Erro no JavaScript: ${error.message}.`);
    
    } finally {
        loadingIndicator.classList.add('hidden');
        submitButton.disabled = false;
    }
});

function displayResults(data) {
    const category = data.category.toLowerCase();
    
    resultCategory.textContent = data.category;

    resultCategory.className = ''; 
    resultCategory.classList.add('badge');

    if (category.includes('produtivo')) {
        resultCategory.classList.add('badge--productive');
    } else if (category.includes('improdutivo')) {
        resultCategory.classList.add('badge--unproductive');
    } else if (category.includes('neutro')) {
        resultCategory.classList.add('badge--neutral');
    } else { 
        resultCategory.classList.add('badge--error');
    }
    
    resultResponse.textContent = data.suggested_response;
    resultArea.classList.remove('hidden');
    saveToHistory(data); 
    renderHistory();
}

function displayError(errorMessage) {
    resultCategory.textContent = 'Erro';

    resultCategory.className = '';
    resultCategory.classList.add('badge', 'badge--error');

    resultResponse.textContent = errorMessage;
    resultArea.classList.remove('hidden');
}

copyButton.addEventListener('click', () => {
    const responseText = resultResponse.textContent;
    navigator.clipboard.writeText(responseText)
        .then(() => {
            copyButton.textContent = 'Copiado!';
            setTimeout(() => {
                copyButton.textContent = 'Copiar';
            }, 2000); 
        })
        .catch(err => {
            console.error('Erro ao copiar texto: ', err);
        });
});

function saveToHistory(analysisData) {
    let history = JSON.parse(localStorage.getItem('emailHistory')) || [];

    history.unshift(analysisData);

    if (history.length > MAX_HISTORY_ITEMS) {
        history = history.slice(0, MAX_HISTORY_ITEMS);
    }
    localStorage.setItem('emailHistory', JSON.stringify(history));
}

function renderHistory() {
    const history = JSON.parse(localStorage.getItem('emailHistory')) || [];

    if (history.length === 0) {
        historySection.classList.add('hidden');
        return;
    }

    historySection.classList.remove('hidden');
    historyEmptyMessage.classList.add('hidden');
    historyList.innerHTML = ''; 

    history.forEach(item => {
        const listItem = document.createElement('li');
        listItem.className = 'history-item';

        const categoryBadge = document.createElement('span');
        categoryBadge.textContent = item.category;
        categoryBadge.className = 'badge';

        const categoryLower = item.category.toLowerCase();

        if (categoryLower.includes('improdutivo')) {
            categoryBadge.classList.add('badge--unproductive');
        } else if (categoryLower.includes('produtivo')) {
            categoryBadge.classList.add('badge--productive');
        } else if (categoryLower.includes('neutro')) {
            categoryBadge.classList.add('badge--neutral');
        } else {
            categoryBadge.classList.add('badge--error');
        }

        const responseDiv = document.createElement('div');
        responseDiv.className = 'response-text';
        responseDiv.textContent = item.suggested_response;

        listItem.appendChild(categoryBadge);
        listItem.appendChild(responseDiv);
        
        historyList.appendChild(listItem);
    });
}

document.addEventListener('DOMContentLoaded', renderHistory);

