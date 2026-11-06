# Exercício 7 - Refatoração
# Código 2: Controle de lanchonete

VALOR_MINIMO_DESCONTO = 100
PERCENTUAL_DESCONTO = 0.10

# Cada pedido é uma lista de itens. A lista de pedidos guarda todos eles.
pedidos = [
    [
        {"nome": "Hamburguer", "preco": 25, "quantidade": 2},
        {"nome": "Suco", "preco": 8, "quantidade": 3},
        {"nome": "Batata", "preco": 15, "quantidade": 2},
    ],
    [
        {"nome": "Pizza", "preco": 45, "quantidade": 2},
        {"nome": "Refrigerante", "preco": 7, "quantidade": 2},
    ],
]


def validar_item(item):
    if item["preco"] < 0 or item["quantidade"] <= 0:
        raise ValueError(f"Item inválido: {item['nome']}")


def calcular_total_item(preco, quantidade):
    return preco * quantidade


def calcular_subtotal(itens):
    return sum(calcular_total_item(i["preco"], i["quantidade"]) for i in itens)


def calcular_desconto(subtotal):
    # A regra do desconto agora está em um lugar só (antes era repetida).
    if subtotal >= VALOR_MINIMO_DESCONTO:
        return subtotal * PERCENTUAL_DESCONTO
    return 0


def exibir_pedido(itens):
    print("=== PEDIDO ===")
    for item in itens:
        validar_item(item)
        total_item = calcular_total_item(item["preco"], item["quantidade"])
        print(item["nome"], item["quantidade"], total_item)

    subtotal = calcular_subtotal(itens)
    desconto = calcular_desconto(subtotal)
    total = subtotal - desconto

    print("Subtotal:", subtotal)
    print("Desconto:", desconto)
    print("Total:", total)

    if desconto > 0:
        print("Desconto aplicado")


def main():
    for pedido in pedidos:
        exibir_pedido(pedido)


main()
