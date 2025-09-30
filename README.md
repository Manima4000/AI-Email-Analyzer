# Classificador de E-mails com IA 📧✨

![Badge de Status](https://img.shields.io/badge/status-funcional-brightgreen)
![Badge do Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Badge do FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![Badge do Docker](https://img.shields.io/badge/Docker-conteinerizado-blue)


> Um classificador de e-mails inteligente que utiliza a API do Google Gemini para categorizar mensagens e sugerir respostas automáticas, tudo através de uma interface web limpa e moderna. O projeto é totalmente containerizado com Docker, garantindo uma execução fácil e consistente em qualquer ambiente.


---

## 📚 Tabela de Conteúdos

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
* [Próximos Passos](#-próximos-passos)
* [Contato](#-contato)

---

## 🎯 Sobre o Projeto

Este projeto simula uma ferramenta de automação e produtividade. A aplicação permite que um usuário cole o texto de um e-mail ou faça o upload de um arquivo (`.txt`/`.pdf`) e, em segundos, receba uma análise gerada por IA sobre o conteúdo, além de uma sugestão de resposta.

O objetivo era construir uma aplicação full-stack completa, demonstrando boas práticas de desenvolvimento, como:
* **Containerização:** Uso de Docker e Docker Compose para garantir portabilidade e facilidade de execução.
* **Arquitetura Desacoplada:** Frontend e backend como serviços independentes.
* **Qualidade de Código:** Cobertura de testes automatizados com Pytest.
* **Configuração Flexível:** Uso de variáveis de ambiente (`.env`) para gerenciar chaves e configurações.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python, FastAPI, Uvicorn
* **Inteligência Artificial:** Google Gemini Pro API
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS), NGINX
* **Testes:** Pytest, pytest-asyncio
* **Containerização:** Docker, Docker Compose
* **Deploy:** Vercel (Frontend), Render (Backend)

---

## ✨ Principais Features

* **Análise por IA:** Sugestão de respostas via Google Gemini.
* **Múltiplos Formatos de Entrada:** Suporte para texto colado e upload de arquivos `.txt` e `.pdf`.
* **Interface Reativa:** Feedback visual de "carregando" durante o processamento.
* **Tema Claro e Escuro (Dark Mode):** Com persistência da escolha do usuário.
* **Modelo de IA Configurável:** Permite a troca fácil do modelo Gemini via variáveis de ambiente.
* **Execução Simplificada:** O projeto inteiro (frontend e backend) sobe com um único comando `docker-compose up`.
* **Cobertura de Testes:** Testes de unidade e integração para garantir a robustez da API.

---

## 🚀 Como Rodar o Projeto Localmente

Siga as instruções abaixo para ter o projeto rodando na sua máquina em segundos.

### Pré-requisitos
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/products/docker-desktop/) e [Docker Compose](https://docs.docker.com/compose/install/)

### Instruções (Docker)

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Configure suas variáveis de ambiente:**
    * Na pasta `backend`, crie uma cópia do arquivo `.env.example` e renomeie-a para `.env`.
    * Abra o arquivo `.env` e preencha as variáveis:
        ```env
        GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"

        MODEL_NAME="gemini-pro" #Pode escolher o modelo de sua preferência
        ```

3.  **Suba os containers com Docker Compose:**
    * Na **pasta raiz do projeto**, execute:
    ```bash
    docker-compose up --build
    ```
    * O Docker irá construir a imagem do backend, baixar a do frontend e iniciar os dois serviços.

4.  **Acesse a aplicação:**
    * **Frontend:** Abra seu navegador e acesse **`http://localhost:5500`**.
    * **Backend API Docs:** A documentação interativa da API estará disponível em **`http://localhost:8000/docs`**.

---

## ✅ Rodando os Testes

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

## ⚙️ Configuração Avançada

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

## ☁️ Estratégia de Deploy

* **Frontend (Vercel):** O conteúdo da pasta `frontend` pode ser implantado como um "Static Site" na Vercel.
* **Backend (Render):** O backend na pasta `backend` é containerizado e pode ser implantado como um "Web Service" na plataforma Render.

---

## 🧭 Próximos Passos
* [ ] Histórico de análises salvo no navegador.
* [ ] Opção de ajustar o "tom" da resposta sugerida (Formal, Amigável, etc.).
* [ ] CI/CD com GitHub Actions para rodar os testes automaticamente.

---

## 👤 Contato

**[Seu Nome]**

* **LinkedIn:** `[Link para o seu LinkedIn]`
* **GitHub:** `[Link para o seu GitHub]`
* **E-mail:** `[Seu E-mail]`
