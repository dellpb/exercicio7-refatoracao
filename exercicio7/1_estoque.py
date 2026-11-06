# Exercício 7 - Refatoração
# Código 1: Controle de estoque para loja

LIMITE_ESTOQUE_BAIXO = 5

# Antes eram 9 variáveis soltas (n1, q1, p1...). Agora é uma lista de produtos.
produtos = [
    {"nome": "Teclado", "quantidade": 3, "preco": 80},
    {"nome": "Mouse", "quantidade": 12, "preco": 40},
    {"nome": "Monitor", "quantidade": 4, "preco": 650},
]


def validar_produto(produto):
    """Não deixa cadastrar quantidade ou preço negativo."""
    if produto["quantidade"] < 0 or produto["preco"] < 0:
        raise ValueError(f"Dados inválidos para o produto {produto['nome']}")


def calcular_valor_em_estoque(quantidade, preco):
    return quantidade * preco


def estoque_esta_baixo(quantidade):
    return quantidade < LIMITE_ESTOQUE_BAIXO


def exibir_produto(produto):
    valor = calcular_valor_em_estoque(produto["quantidade"], produto["preco"])
    print("Produto:", produto["nome"])
    print("Estoque:", produto["quantidade"])
    print("Valor:", valor)

    if estoque_esta_baixo(produto["quantidade"]):
        print("Estoque baixo")
    else:
        print("Estoque normal")


def exibir_alertas_de_compra(lista_produtos):
    for produto in lista_produtos:
        if estoque_esta_baixo(produto["quantidade"]):
            print("Comprar mais", produto["nome"])


def main():
    for produto in produtos:
        validar_produto(produto)
        exibir_produto(produto)

    exibir_alertas_de_compra(produtos)


main()
