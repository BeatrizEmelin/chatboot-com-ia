🤖 ChatBot com IA (Gemini + Streamlit)

Este é um projeto de chatbot interativo que utiliza o modelo de linguagem Gemini do Google para gerar respostas inteligentes. A interface foi construída utilizando Streamlit, permitindo uma experiência de chat fluida e moderna diretamente no navegador.

## 🚀 Funcionalidades

* **Interação em Tempo Real:** Interface de chat limpa e responsiva.
* **Memória de Conversa:** Utiliza o `session_state` do Streamlit para manter o histórico da conversa durante a sessão.
* **Integração com Gemini:** Conectado à API da Google Generative AI para processamento de linguagem natural.
* **Feedback Visual:** Spinner de carregamento enquanto a IA gera a resposta.
* **Tratamento de Erros:** Sistema robusto para identificar problemas com chaves de API ou conexão.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Interface Web: Streamlit

Modelo de IA: Google Gemini API

Gerenciamento de Segredos: Streamlit Secrets (para proteção da API Key).

📋 Pré-requisitos
Antes de começar, você precisará de uma chave de API do Google Gemini. Você pode obtê-la no Google AI Studio.

🔧 Instalação e Configuração
Clone o repositório:

Bash

git clone https://github.com/beatriz-emelin/chatboot-com-ia.git
cd seu-repositorio
Instale as dependências:

Bash

pip install streamlit google-generativeai
Configuração da API Key: Crie uma pasta chamada .streamlit na raiz do projeto e, dentro dela, um arquivo secrets.toml:

Ini, TOML

# .streamlit/secrets.toml
GOOGLE_API_KEY = "SUA_CHAVE_AQUI"
Execute a aplicação:

Bash

streamlit run main.py
📂 Estrutura do Código
O arquivo principal main.py contém:

Configuração do modelo gemini-1.5-flash.

Lógica de persistência de histórico de mensagens.

Conversão de formatos de "role" (usuário/modelo) para compatibilidade com a API do Google.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
