# 🤖 ChatBot com IA (Gemini + Streamlit)

Este é um projeto de chatbot interativo que utiliza o modelo de linguagem Gemini do Google para gerar respostas inteligentes. A interface foi construída utilizando Streamlit, permitindo uma experiência de chat fluida e moderna diretamente no navegador.

## 🚀 Funcionalidades

* **Interação em Tempo Real:** Interface de chat limpa e responsiva.
* **Memória de Conversa:** Utiliza o `session_state` do Streamlit para manter o histórico da conversa durante a sessão.
* **Integração com Gemini:** Conectado à API da Google Generative AI para processamento de linguagem natural.
* **Feedback Visual:** Spinner de carregamento enquanto a IA gera a resposta.
* **Tratamento de Erros:** Sistema robusto para identificar problemas com chaves de API ou conexão.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Interface Web:** Streamlit
* **Modelo de IA:** Google Gemini API
* **Gerenciamento de Segredos:** Streamlit Secrets (para proteção da API Key)

## 📋 Pré-requisitos

Antes de começar, você precisará de uma chave de API do Google Gemini. Você pode obtê-la gratuitamente no [Google AI Studio](https://aistudio.google.com/).

## 🔧 Instalação e Configuração

1. **Clone o repositório:**
```bash
git clone https://github.com/beatriz-emelin/chatboot-com-ia.git
cd chatboot-com-ia
```
2. **Instale as dependências:**
```bash
pip install streamlit google-generativeai
```

3. **Configuração da API Key:** Crie uma pasta chamada .streamlit na raiz do projeto e, dentro dela, um arquivo secrets.toml:
Ini, TOML
```bash
# .streamlit/secrets.toml
GOOGLE_API_KEY = "SUA_CHAVE_AQUI"
```

4. **Execute a aplicação:**
```bash
streamlit run main.py
```

## 📂 Estrutura do Código

O arquivo principal `main.py` contém:

* **Configuração do modelo:** utiliza o `gemini-1.5-flash`.
* **Lógica de persistência:** mantém o histórico de mensagens da sessão através do `st.session_state`.
* **Conversão de formatos:** adapta as "roles" (usuário/assistente) para o formato compatível com a API do Google (user/model).

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
