# Classificador de E-mails com IA 

![Badge de Status](https://img.shields.io/badge/status-funcional-brightgreen)
![Badge do Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Badge do FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![Badge do Docker](https://img.shields.io/badge/Docker-conteinerizado-blue)


> Um classificador de e-mails inteligente que utiliza a API do Google Gemini para categorizar mensagens e sugerir respostas automáticas. O projeto é totalmente containerizado com Docker e possui uma interface web limpa e moderna.


**🔗 Link para a Demo Ao Vivo:** `https://ai-email-frontend-nine.vercel.app/`

---

## Tabela de Conteúdos

* [Sobre o Projeto](#-sobre-o-projeto)
* [Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [Principais Features](#-principais-features)
* [Como Rodar o Projeto Localmente](#-como-rodar-o-projeto-localmente)
  * [Pré-requisitos](#pré-requisitos)
  * [Instruções (Docker)](#instruções-docker)
* [Rodando os Testes](#-rodando-os-testes)
* [Configuração Avançada](#-configuração-avançada)
  * [Escolhendo o Modelo de IA](#escolhendo-o-modelo-de-ia)
  * [Rodando Manualmente (Sem Docker)](#rodando-manualmente-sem-docker)
* [Estratégia de Deploy](#-estratégia-de-deploy)


---

## Sobre o Projeto

Este projeto simula uma ferramenta de automação e produtividade. A aplicação permite que um usuário cole o texto de um e-mail ou faça o upload de um arquivo (`.txt`/`.pdf`) e, em segundos, receba uma análise gerada por IA sobre o conteúdo, além de uma sugestão de resposta.

O objetivo era construir uma aplicação full-stack completa, demonstrando boas práticas de desenvolvimento, como:
* **Containerização:** Uso de Docker e Docker Compose para garantir portabilidade e facilidade de execução.
* **Arquitetura Desacoplada:** Frontend e backend como serviços independentes.
* **Qualidade de Código:** Cobertura de testes automatizados com Pytest.
* **Configuração Flexível:** Uso de variáveis de ambiente (`.env`) para gerenciar chaves e configurações.

---

## Tecnologias Utilizadas

* **Backend:** Python, FastAPI, Uvicorn, BeautifulSoup4
* **Inteligência Artificial:** Google Gemini Pro API
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS), NGINX
* **Testes:** Pytest, pytest-asyncio
* **Containerização:** Docker, Docker Compose
* **Deploy:** Vercel (Frontend), Render (Backend)

---

## Principais Features

* **Análise por IA:** Sugestão de respostas via Google Gemini.
* **Múltiplos Formatos de Entrada:** Suporte para texto colado e upload de arquivos `.txt` e `.pdf`.
* **Pré-processamento Inteligente de Texto:** Limpeza automática de tags HTML e respostas de e-mails antigos.
* **Interface Reativa:** Feedback visual de "carregando" durante o processamento.
* **Tema Claro e Escuro (Dark Mode):** Com persistência da escolha do usuário.
* **Modelo de IA Configurável:** Permite a troca fácil do modelo Gemini.
* **Execução Simplificada:** O projeto inteiro (frontend e backend) sobe com um único comando `docker-compose up`.
* **Cobertura de Testes:** Testes de unidade e integração para garantir a robustez da API.

---

## 🚀 Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e executar a aplicação completa em seu ambiente de desenvolvimento local.

### Pré-requisitos
* [Git](https://git-scm.com/)
* [Python 3.11+](https://www.python.org/)
* [Docker](https://www.docker.com/products/docker-desktop/) e [Docker Compose](https://docs.docker.com/compose/install/)

### Passo 1: Clone o Repositório
```bash
git clone [https://github.com/Manima4000/AI-Email-Analyzer.git](https://github.com/Manima4000/AI-Email-Analyzer.git)
cd AI-Email-Analyzer
```

### Passo 2: Configure o Backend
Crie o arquivo de variáveis de ambiente para o backend.

* Na pasta `backend`, crie uma cópia do arquivo `.env.example` e renomeie-a para `.env`.
* Abra o arquivo `.env` e preencha as variáveis:
    ```env
    GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"
    MODEL_NAME="gemini-pro"
    ```

### Passo 3: Configure o Frontend para o Ambiente Local
O código no repositório está configurado para usar a API em produção. Para desenvolvimento local, você precisa apontar o frontend para o seu backend local.

* Abra o arquivo `frontend/script.js`.
* Encontre a linha que define a URL da API.
* Comente a linha da URL de produção e descomente a linha da URL local:
    ```javascript
    // const apiUrl = '[https://ai-email-backend-awbw.onrender.com//api/v1/classify-email](https://ai-email-backend-awbw.onrender.com//api/v1/classify-email)'; // <-- URL de Produção
    const apiUrl = '[http://127.0.0.1:8000/api/v1/classify-email](http://127.0.0.1:8000/api/v1/classify-email)'; // <-- URL Local para Desenvolvimento
    ```

### Passo 4: Execute a Aplicação (Docker ou Manual)

#### Método A: Docker (Recomendado)
Com o Docker, você sobe o frontend e o backend com um único comando.

1.  Verifique se o Docker Desktop está rodando.
2.  Na **pasta raiz do projeto**, execute:
    ```bash
    docker-compose up --build
    ```
3.  Acesse a aplicação:
    * **Frontend:** **`http://localhost:5500`**
    * **Backend Docs:** **`http://localhost:8000/docs`**

#### Método B: Manualmente
Execute o backend e o frontend em terminais separados.

1.  **Terminal 1 (Backend):**
    ```bash
    cd backend
    python -m venv .venv
    # Windows: .\.venv\Scripts\activate | macOS/Linux: source .venv/bin/activate
    pip install -r requirements.txt
    uvicorn app.main:app --reload
    ```

2.  **Terminal 2 (Frontend):**
    ```bash
    cd frontend
    python -m http.server 5500
    ```
3.  Acesse o frontend em **`http://localhost:5500`**.

---

## Rodando os Testes

Para garantir que a lógica do backend está funcionando corretamente, você pode rodar a suíte de testes automatizados.

1.  **Siga os passos de configuração do "Método Manual"** (veja na seção de Configuração Avançada) para criar e ativar o ambiente virtual (`.venv`) e instalar as dependências (`pip install -r requirements.txt`).

2.  **Execute o Pytest:**
    * Na pasta `backend`, execute o comando apropriado para o seu sistema operacional:

    * **No Windows (PowerShell):**
        ```powershell
        $env:PYTHONPATH="."; pytest -v
        ```

    * **No Windows (CMD):**
        ```powershell
        set PYTHONPATH=.
        pytest -v
        ```

    * **No macOS/Linux:**
        ```bash
        PYTHONPATH=. pytest -v
        ```

---

## Configuração Avançada

### Escolhendo o Modelo de IA
A disponibilidade dos modelos do Gemini pode variar. Incluímos um script para você verificar quais modelos sua chave de API pode acessar.

1.  Configure o ambiente do backend manualmente (veja o próximo passo).
2.  Na pasta `backend`, execute o script de verificação:
    ```bash
    python check_models.py
    ```
3.  O terminal listará os modelos disponíveis. Copie o nome de um deles e cole como o valor da variável `MODEL_NAME` no seu arquivo `.env`.

### Rodando Manualmente (Sem Docker)

1.  **Configure o Backend:**
    ```bash
    cd backend
    python -m venv .venv
    # Windows: .\.venv\Scripts\activate | macOS/Linux: source .venv/bin/activate

    # O arquivo requirements.txt lista todas as bibliotecas Python que o projeto precisa.
    pip install -r requirements.txt

    # Crie e configure o arquivo .env (como no método Docker)
    uvicorn app.main:app --reload
    ```
    * O backend estará rodando em `http://localhost:8000`.

2.  **Rode o Frontend:**
    * Use uma extensão como o **"Live Server"** no VS Code ou inicie um servidor Python na pasta `frontend`:
    ```bash
    cd frontend
    python -m http.server 5500
    ```
    * Acesse `http://localhost:5500`.

---

## Estratégia de Deploy

* **Frontend (Vercel):** O conteúdo da pasta `frontend` pode ser implantado como um "Static Site" na Vercel.
* **Backend (Render):** O backend na pasta `backend` é containerizado e pode ser implantado como um "Web Service" na plataforma Render.

---

