# Classificador de E-mails com IA 📧✨

![Badge de Status](https://img.shields.io/badge/status-funcional-brightgreen)
![Badge do Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Badge do FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![Badge do Frontend](https://img.shields.io/badge/Frontend-Vanilla%20JS-orange)

![GIF da Aplicação em Funcionamento](https://via.placeholder.com/800x400.png?text=Insira+um+GIF+da+sua+aplicação+aqui)

> Um classificador de e-mails inteligente que utiliza a API do Google Gemini para categorizar mensagens como "Produtivas" ou "Improdutivas" e sugere respostas automáticas, tudo através de uma interface web limpa e moderna.

**🔗 Link para a Demo Ao Vivo:** `[EM BREVE]`

---

## 📚 Tabela de Conteúdos

* [Sobre o Projeto](#-sobre-o-projeto)
* [Tecnologias Utilizadas](#-tecnologias-utilizadas)
* [Principais Features](#-principais-features)
* [Como Rodar o Projeto Localmente](#-como-rodar-o-projeto-localmente)
  * [Pré-requisitos](#pré-requisitos)
  * [Método 1: Docker (Recomendado)](#método-1-docker-recomendado)
  * [Método 2: Manualmente](#método-2-manualmente)
* [Escolhendo o Modelo de IA](#-escolhendo-o-modelo-de-ia-opcional)
* [Rodando os Testes](#-rodando-os-testes)
* [Estratégia de Deploy](#-estratégia-de-deploy)
* [Próximos Passos](#-próximos-passos)
* [Contato](#-contato)

---

## 🎯 Sobre o Projeto

Este projeto foi desenvolvido para simular uma ferramenta de automação e produtividade. A aplicação permite que um usuário cole o texto de um e-mail ou faça o upload de um arquivo (`.txt`/`.pdf`) e, em segundos, receba uma análise gerada por IA sobre o conteúdo, além de uma sugestão de resposta pronta para uso.

O objetivo era construir uma aplicação full-stack completa, demonstrando boas práticas de desenvolvimento, como:
* Arquitetura de microsserviços desacoplada (frontend e backend).
* Testes automatizados para garantir a qualidade do código.
* Configuração flexível através de variáveis de ambiente.
* Desenvolvimento orientado a uma experiência de usuário limpa e moderna.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python, FastAPI, Uvicorn
* **Inteligência Artificial:** Google Gemini Pro API
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS)
* **Testes:** Pytest, pytest-asyncio
* **Containerização:** Docker, Docker Compose
* **Deploy:** Vercel (Frontend), Render (Backend)

---

## ✨ Principais Features

* **Análise por IA:** Classificação de e-mails e sugestão de respostas via Google Gemini.
* **Múltiplos Formatos de Entrada:** Suporte para texto colado, upload de arquivos `.txt` e `.pdf`.
* **Interface Reativa:** Feedback visual de "carregando" durante o processamento.
* **Tema Claro e Escuro (Dark Mode):** Com persistência da escolha do usuário.
* **Backend Assíncrono:** Construído com FastAPI para alta performance.
* **Modelo de IA Configurável:** Permite a troca fácil do modelo Gemini via variáveis de ambiente.
* **Cobertura de Testes:** Testes de unidade e integração para garantir a robustez da API.

---

## 🚀 Como Rodar o Projeto Localmente

Siga as instruções abaixo para ter o projeto rodando na sua máquina.

### Pré-requisitos
* [Git](https://git-scm.com/)
* [Python 3.11+](https://www.python.org/)
* [Docker](https://www.docker.com/products/docker-desktop/) e [Docker Compose](https://docs.docker.com/compose/install/) (para o método recomendado)

### Método 1: Docker (Recomendado)

Esta é a forma mais simples e rápida. O Docker cuida de toda a configuração para você.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Configure suas variáveis de ambiente:** * Vá para a pasta `backend`.
    * Crie uma cópia do arquivo `.env.example` e renomeie-a para `.env`.
    * Abra o arquivo `.env` e preencha as variáveis:
        ```env
        # Cole aqui a chave que você obteve no Google AI Studio
        GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"

        # (Opcional) Nome do modelo a ser usado. 'gemini-pro' é um padrão seguro.
        MODEL_NAME="gemini-pro"
        ```

3.  **Suba os containers com Docker Compose:**
    * Na pasta raiz do projeto, execute:
    ```bash
    docker-compose up --build
    ```
    * O Docker irá construir a imagem do backend e iniciar o servidor.

4.  **Acesse a aplicação:**
    * **Frontend:** Abra seu navegador e acesse `http://localhost:5500` (ou abra o arquivo `frontend/index.html` diretamente).
    * **Backend API Docs:** A documentação interativa da API estará disponível em `http://localhost:8000/docs`.

### Método 2: Manualmente

1.  **Clone o repositório e navegue até ele.**

2.  **Configure e rode o Backend:**
    ```bash
    cd backend

    # Crie e ative o ambiente virtual
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate

    # O arquivo requirements.txt lista todas as bibliotecas Python que o projeto precisa.
    # Instale todas de uma vez com o comando abaixo:
    pip install -r requirements.txt # <-- ATUALIZADO

    # Crie o arquivo .env e adicione suas chaves (siga o passo 2 do método Docker)

    # Inicie o servidor
    uvicorn app.main:app --reload
    ```
    * O backend estará rodando em `http://localhost:8000`.

3.  **Rode o Frontend:**
    * A maneira mais fácil é usar uma extensão como o **"Live Server"** no VS Code. Clique com o botão direito no arquivo `frontend/index.html` e selecione "Open with Live Server".
    * Alternativamente, abra o arquivo `frontend/index.html` diretamente no seu navegador.

---

## ⚙️ Escolhendo o Modelo de IA (Opcional)

A disponibilidade dos modelos do Gemini pode variar por conta ou região. Incluímos um script para você verificar quais modelos sua chave de API pode acessar e escolher o melhor.

1.  **Siga os passos do "Método 2: Manualmente"** para configurar o ambiente do backend (ativar o `.venv` e instalar as dependências com `pip install -r requirements.txt`).

2.  **Rode o script de verificação:**
    * Na pasta `backend`, execute o comando:
    ```bash
    python check_models.py
    ```

3.  **Veja a saída:** O terminal listará os modelos disponíveis, algo como:
    ```
    Listando modelos disponíveis que suportam 'generateContent':
    models/gemini-pro
    models/gemini-1.0-pro
    models/gemini-1.5-flash-latest
    Script concluído.
    ```

4.  **Atualize seu arquivo `.env`:** Copie o nome de um dos modelos da lista (apenas a parte final, ex: `gemini-pro`) e cole-o como o valor da variável `MODEL_NAME` no seu arquivo `.env`.

---

## ✅ Rodando os Testes

Para garantir que a lógica do backend está funcionando corretamente, você pode rodar a suíte de testes automatizados.

1.  Navegue até a pasta `backend` e ative o ambiente virtual.
2.  Execute o `pytest`:
    ```bash
    # A partir da pasta 'backend'
    pytest
    ```

---

## ☁️ Estratégia de Deploy

A aplicação é projetada para um deploy moderno e desacoplado:

* **Frontend (Vercel):** O conteúdo da pasta `frontend` pode ser implantado como um "Static Site" na Vercel. Basta conectar seu repositório GitHub e a Vercel cuidará do resto.

* **Backend (Render):** O backend na pasta `backend` é containerizado com Docker. A melhor abordagem é implantá-lo como um "Web Service" na plataforma Render, que se integra perfeitamente com o Docker. A Render fornecerá uma URL pública para a sua API, que você deverá configurar no seu `script.js` antes de fazer o deploy do frontend.

---

## 🧭 Próximos Passos

Recursos planejados para futuras versões:
* [ ] Streaming da resposta da IA (efeito "ChatGPT").
* [ ] Histórico de análises salvo no navegador.
* [ ] Opção de ajustar o "tom" da resposta sugerida (Formal, Amigável, etc.).
* [ ] CI/CD com GitHub Actions para rodar os testes automaticamente.

---

## 👤 Contato

**[Seu Nome]**

* **LinkedIn:** `[Link para o seu LinkedIn]`
* **GitHub:** `[Link para o seu GitHub]`
* **E-mail:** `[Seu E-mail]`