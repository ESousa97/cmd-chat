# Guia de Contribuição 

Bem-vindo ao nosso projeto! Agradecemos o tempo que você dedica a nos ajudar a melhorar o cmd-chat. Temos uma lista de diretrizes bem diretas para alinhar suas PRs.

## Contribuindo

Para configurar um ambiente de desenvolvimento e começar a programar:

1. Dê um Fork no projeto em https://github.com/dinosaurtirex/cmd-chat.
2. Ative um ambiente virtual e use `pip install -e ".[dev]"`. Opcionalmente você precisará instalar as dependências ruff/pytest do `pyproject.toml`.
3. Crie uma branch clara: `git checkout -b feat/nova-feature`.
4. Codifique a sua ideia. Siga atentamente a nossa convenção local: usamos `ruff` para padronizar todo o Python. Execute sempre `ruff format .` e `ruff check --fix .` antes do commit.
5. Siga semântica de commits: `feat`, `fix`, `refactor`, `docs`, `chore`, `ci`, `test`, `perf`, `security` (Ex: `fix: resolver vazamento x no core client`).
6. Abra o PR! Siga nosso template padrão que será injetado do `.github/PULL_REQUEST_TEMPLATE.md`. Responderemos rápido!

## Testes Localmente
Sempre rode `pytest tests/` no repositório antes de submeter uma issue. Garantir cobertura é ideal.

Obrigado por ajudar a comunidade open-source Python!
