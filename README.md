# Exercício 7 - Refatoração

**Curso:** Análise e Desenvolvimento de Sistemas
**Disciplina:** Coding
**Professor:** Joseph Donald

Refatoração de 4 códigos em Python com problemas de qualidade: nomes ruins, código repetido, responsabilidades misturadas e falta de validação.

## O que foi feito em todos os códigos

- Nomes claros para variáveis e funções
- Funções separadas por responsabilidade
- Código repetido eliminado
- Dados organizados em listas
- Validação simples dos dados
- Execução no terminal, com resultado conferido

## Códigos

| Arquivo | Tema | O que mudou |
|---|---|---|
| [`1_estoque.py`](exercicio7/1_estoque.py) | Controle de estoque | Regra do estoque baixo em uma função só |
| [`2_lanchonete.py`](exercicio7/2_lanchonete.py) | Controle de lanchonete | Desconto calculado em um lugar só e pedidos exibidos pela mesma função |
| [`3_despesas.py`](exercicio7/3_despesas.py) | Despesas pessoais | 8 `if` repetidos viraram uma função |
| [`4_papelaria.py`](exercicio7/4_papelaria.py) | Controle de papelaria | `for` no lugar de prints repetidos e parâmetro inútil removido |

## Como executar

```bash
cd exercicio7
python 1_estoque.py
python 2_lanchonete.py
python 3_despesas.py
python 4_papelaria.py
```

No Windows, se `python` não funcionar, use `py`.

## Resultado

Os 4 programas foram executados no terminal e comparados com os originais. Os resultados continuam corretos. No código 2 só mudou o formato do segundo pedido, que agora aparece igual ao primeiro.
