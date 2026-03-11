# Changelog

Todas observações em relação a novas versões serão documentados estritamente usando [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

O versionamento segue rigoroso os padrões globais da [SemVer](https://semver.org/lang/pt-BR/2.0.0/).

## [1.1.22] - 2026-03-10
### Added
- Documentação extensa (`README`, `BASELINE`, `FINAL`, `CONTRIBUTING`, `SECURITY`).
- Modelagem Pydantic robusta (proteção da entrada web de sockets).
- Setup via `pyproject.toml` focado nas novas versões das bibliotecas, unificando dependências Python modernas.
- `.github` completo e pronto contendo Issue e PR templates.
- Linter base (`Ruff`) habilitado.

### Changed
- Refatoração dos inputs no WebSockets (evitando a execução em nível AST mal intencionada).
- Migração de nomenclatura de constantes (ex. `PUBLIC_KEY` alterado com clareza conceitual para `SHARED_SYMMETRIC_KEY`).

### Removed
- Executáveis locais desnecessários.
- Rastro de scripts depreciados como os velhos scripts `setup.py` customizados.
