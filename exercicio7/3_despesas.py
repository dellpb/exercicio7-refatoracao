# Exercício 7 - Refatoração
# Código 3: Despesas pessoais

RENDA_MENSAL = 1500

despesas = [
    {"nome": "Internet", "valor": 100, "tipo": "Fixa"},
    {"nome": "Alimentacao", "valor": 450, "tipo": "Variavel"},
    {"nome": "Energia", "valor": 180, "tipo": "Fixa"},
    {"nome": "Transporte", "valor": 220, "tipo": "Variavel"},
]


def validar_despesa(despesa):
    if despesa["valor"] < 0:
        raise ValueError(f"Valor inválido para {despesa['nome']}")
    if despesa["tipo"] not in ("Fixa", "Variavel"):
        raise ValueError(f"Tipo inválido para {despesa['nome']}")


def calcular_total(lista_despesas):
    return sum(d["valor"] for d in lista_despesas)


def calcular_total_por_tipo(lista_despesas, tipo):
    # Uma função só serve para fixas e variáveis (antes eram 2 blocos repetidos).
    return sum(d["valor"] for d in lista_despesas if d["tipo"] == tipo)


def calcular_saldo(renda, total_gasto):
    return renda - total_gasto


def exibir_relatorio(lista_despesas):
    print("Relatorio de gastos")
    for d in lista_despesas:
        print(d["nome"], d["valor"], d["tipo"])
    print("Total:", calcular_total(lista_despesas))


def main():
    for despesa in despesas:
        validar_despesa(despesa)

    exibir_relatorio(despesas)

    print("Despesas fixas:", calcular_total_por_tipo(despesas, "Fixa"))
    print("Despesas variaveis:", calcular_total_por_tipo(despesas, "Variavel"))

    saldo = calcular_saldo(RENDA_MENSAL, calcular_total(despesas))
    print("Renda:", RENDA_MENSAL)
    print("Saldo:", saldo)

    if saldo < 0:
        print("Gastos acima da renda")
    else:
        print("Gastos dentro da renda")


main()
