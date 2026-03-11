# cmd-chat

> Um chat de linha de comando seguro usando RSA e Fernet (criptografia end-to-end), construído sobre Sanic e WebSockets.

![CI](https://github.com/dinosaurtirex/cmd-chat/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/github/license/dinosaurtirex/cmd-chat)
![Python](https://img.shields.io/badge/python-%3E%3D3.10-blue)
![Last Commit](https://img.shields.io/github/last-commit/dinosaurtirex/cmd-chat)
![CodeFactor](https://www.codefactor.io/repository/github/dinosaurtirex/cmd-chat/badge)

O `cmd-chat` permite que desenvolvedores criem salas de chat através do terminal. Todas as mensagens são encriptadas usando criptografia híbrida: as chaves simétricas (Fernet) são negociadas com segurança através de chaves assimétricas (RSA 512-bit) e cada cliente exibe seu display usando a biblioteca Rich ou renderização padrão.

## Funcionalidades
- 🔒 **Comunicação Encriptada**: RSA para troca segura de chaves + Fernet para a sessão simétrica.
- 🚀 **Asynchronous IO**: Servidor de alta performance construído com Sanic.
- 🎨 **Rich UI**: Terminal limpo e colorido (IP e Username colors).
- 🛠 **Validado e Checado**: Totalmente aderente ao padrão PEP8 moderno (Ruff) e Pydantic.

## Demonstração

![Example Usage](example.gif)

## Stack Tecnológico

| Tecnologia | Função no Projeto |
|---|---|
| **Python 3.10+** | Base Runtime |
| **Sanic** | Servidor Assíncrono para rotas HTTP e WebSockets |
| **Pydantic** | Validação rápida de contratos de payloads de WebSocket |
| **RSA / Cryptography**| Implementação criptográfica |
| **Rich / Colorama** | Interface CLI |

## Pré-requisitos

- Python `>= 3.10`
- `pip` e ambiente virtual

## Instalação e Uso

1. **Clone o repositório** e entre na pasta:
```bash
git clone https://github.com/dinosaurtirex/cmd-chat.git
cd cmd-chat
```

2. **Crie e ative um ambiente virtual:**
```bash
python -m venv venv
# Linux/MacOS
source venv/bin/activate
# Windows
.\venv\Scripts\activate
```

3. **Instale os requisitos:**
```bash
pip install -e .
```

4. **Configuração inicial:**
Crie o seu `.env`:
```bash
cp .env.example .env
```
Ou edite opcionalmente e defina seu `ADMIN_PASSWORD`.

## Como Usar o Chat

O `cmd-chat` instala um executável no seu PATH local. Você também pode rodá-lo utilizando `python cmd_chat.py`.

### Iniciando o Servidor

```bash
cmd_chat serve 127.0.0.1 5000 -p "senha_super_secreta"
```

### Conectando um Cliente

Em um terminal separado (para o cliente), excute:

```bash
cmd_chat connect 127.0.0.1 5000 "senha_super_secreta"
```

O `cmd-chat` agora gera automaticamente um nome de usuário aleatório para você (ex: `SmartFox52`, `BraveLion12`, etc.) ao ingressar no servidor!

Você agora está no chat! Digite suas mensagens e inicie a conversa. 

## Scripts Disponíveis
Se você está contribuindo para o repositório, use os scripts atrelados ao `Makefile` ou diretamente via pip:

| Comando | Descrição |
|---|---|
| `ruff check .` | Roda linting para código |
| `ruff format .` | Formata o código do repositório inteiro |
| `pytest tests/` | Executa a pipeline de testes do repositório |

## API Documentada
A API utiliza chamadas Websocket.
- `/talk` (WS): Envio de mensagens codificadas em Fernet, no formato `{"text": "<enc_msg>", "username": "...", "action": "..."}`
- `/update` (WS): Recebimento contínuo e sincronização da janela de mensagens e usuários logados no formato `{"messages": [...], "users_in_chat": [...]}`.
- `/get_key` (POST/GET): Handshake RSA recebendo um `.pem` public key. 

## Roadmap
- [ ] Integração com banco de dados real (MongoDB ou SQLite) ao invés de memória
- [ ] Configuração de canais customizados
- [ ] Webhook de notificação
- [ ] Adicionar testes E2E com `pytest-asyncio`

## Contribuindo
Esteja livre para melhorar o projeto. Veja o [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes.

## Autor

**dinosaurtirex**

* [Portfólio](https://enoquesousa.vercel.app)
* [GitHub](https://github.com/dinosaurtirex)

## Licença
Este repositório é licenciado através de [MIT](LICENSE).
