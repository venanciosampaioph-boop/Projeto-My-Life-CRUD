# MyLife 2.0

O MyLife é um programa simples de gerenciamento de tarefas feito em Python. Ele foi desenvolvido para praticar conceitos aprendidos durante as aulas, como listas, dicionários, condicionais, estruturas de repetição e manipulação de dados.

## Funcionalidades

- Adicionar tarefas com descrição.
- Visualizar todas as tarefas cadastradas e seus status.
- Concluir tarefas pendentes.
- Excluir tarefas cadastradas.
- Validar descrições vazias ou formadas apenas por espaços.
- Tratar entradas que não sejam números nas opções de concluir e excluir tarefas.

## Como executar

1. Tenha o Python 3 instalado no computador.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute:

```bash
python CRUD.py
```

## Como funciona

As tarefas são armazenadas em uma lista. Cada tarefa é representada por um dicionário com duas informações:

- `descricao`: texto informado pelo usuário.
- `status`: situação da tarefa, inicialmente definida como `Pendente`.

Os dados ficam armazenados apenas enquanto o programa está em execução. Ao fechar o programa, as tarefas cadastradas não são salvas em um arquivo.

## Tecnologias e conceitos

- Python 3
- Listas e dicionários
- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`while` e `for`)
- `enumerate()`
- Tratamento de exceções com `try/except ValueError`
- Métodos de string, como `strip()`
