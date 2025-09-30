// Seleciona os elementos do DOM
const form = document.getElementById('email-form');
const textInput = document.getElementById('email-text');
const fileInput = document.getElementById('email-file');
const submitButton = document.getElementById('submit-button');
const loadingIndicator = document.getElementById('loading-indicator');
const resultArea = document.getElementById('result-area');
const resultCategory = document.getElementById('result-category');
const resultResponse = document.getElementById('result-response');
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;


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
    event.preventDefault(); // Impede o comportamento padrão do formulário

    const text = textInput.value;
    const file = fileInput.files[0];

    // Validação: verifica se pelo menos um campo foi preenchido
    if (!text && !file) {
        alert('Por favor, cole um texto ou selecione um arquivo.');
        return;
    }

    // Validação: impede o envio de ambos os campos
    if (text && file) {
        alert('Por favor, envie apenas texto ou um arquivo, não ambos.');
        return;
    }

    // Prepara os dados para envio
    const formData = new FormData();
    if (text) {
        formData.append('email_text', text);
    } else if (file) {
        formData.append('email_file', file);
    }

    // Atualiza a UI para o estado de "carregando"
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
        console.error("Tipo de Erro:", error.name);      // Ex: TypeError
        console.error("Mensagem:", error.message);    // Ex: Failed to fetch
        console.error("Objeto do Erro:", error);        // O erro completo
        console.error("---------------------------------");
        

        displayError(`Erro no JavaScript: ${error.message}. Verifique o console (F12) para detalhes técnicos.`);
    
    } finally {
        loadingIndicator.classList.add('hidden');
        submitButton.disabled = false;
    }
});

function displayResults(data) {
    resultCategory.textContent = data.category;
    resultResponse.textContent = data.suggested_response;
    resultArea.classList.remove('hidden');
}

function displayError(errorMessage) {
    resultCategory.textContent = 'Erro';
    resultResponse.textContent = errorMessage;
    resultArea.classList.remove('hidden');
}


