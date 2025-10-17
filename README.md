# Automação de Testes - PUC Minas Destaques

## Tecnologias
- Python
- Selenium WebDriver
- Pytest
- Page Object Pattern

## Instalação no Windows
1. Instale o Python ([Download Python para Windows](https://www.python.org/downloads/windows/))
2. Instale o Google Chrome (caso ainda não tenha)
3. Abra o Prompt de Comando (cmd) ou o terminal do VS Code na pasta do projeto

Execute:
```bash
pip install -r requirements.txt
```

## Execução dos Testes no Windows
No Prompt de Comando ou terminal do VS Code, execute:
```bash
pytest
```

## Estrutura
- `pages/` - Page Objects
- `tests/` - Cenários de Teste
- `conftest.py` - Setup do WebDriver

## Cenário Automático
- Verifica se a página de destaques carrega corretamente e se existe ao menos um destaque na lista.

## Observações
- Ajuste os seletores dos elementos conforme o HTML real do site.
- O WebDriver Manager baixa o driver automaticamente, não é necessário baixar manualmente.
