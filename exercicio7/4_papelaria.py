# Exercício 7 - Refatoração
# Código 4: Controle de papelaria

META_DE_VENDAS = 250
VALOR_MINIMO_TAXA = 300
PERCENTUAL_TAXA = 0.05

vendas = [
    {"produto": "Caderno", "preco": 20, "quantidade": 3},
    {"produto": "Caneta", "preco": 2.50, "quantidade": 10},
    {"produto": "Mochila", "preco": 100, "quantidade": 2},
]


def validar_venda(venda):
    if venda["preco"] < 0 or venda["quantidade"] <= 0:
        raise ValueError(f"Venda inválida: {venda['produto']}")


def calcular_total_venda(preco, quantidade):
    # Antes tinha um 3º parâmetro que só multiplicava por 1 (inútil). Tirei.
    return preco * quantidade


def calcular_total_geral(lista_vendas):
    return sum(calcular_total_venda(v["preco"], v["quantidade"]) for v in lista_vendas)


def verificar_meta(total, meta):
    if total >= meta:
        return "Meta atingida"
    return "Meta nao atingida"


def calcular_taxa(total):
    if total > VALOR_MINIMO_TAXA:
        return total * PERCENTUAL_TAXA
    return 0


def exibir_venda(venda):
    print("Produto:", venda["produto"])
    print("Quantidade:", venda["quantidade"])
    print("Total:", calcular_total_venda(venda["preco"], venda["quantidade"]))


def main():
    for venda in vendas:
        validar_venda(venda)
        exibir_venda(venda)

    total_vendas = calcular_total_geral(vendas)
    print("Total das vendas:", total_vendas)
    print(verificar_meta(total_vendas, META_DE_VENDAS))

    taxa = calcular_taxa(total_vendas)
    print("Taxa:", taxa)
    print("Valor final:", total_vendas + taxa)


main()
