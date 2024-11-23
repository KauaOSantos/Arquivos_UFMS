quantidade = int(input())
produtos = []

for _ in range(quantidade):
    produto = input().strip()
    preco = float(input())

    produtoCadastrado = False
    for item in produtos:
        if item[0] == produto:
            print("Produto já cadastrado")
            produtoCadastrado = True
            break

    if not produtoCadastrado:
        produtos.append((produto, preco))

while True:
    produtoBuscado = input().strip()
    if produtoBuscado == "Fim":
        break

    encontrado = False
    for item in produtos:
        if item[0] == produtoBuscado:
            print(item[1]) 
            encontrado = True
            break
    if not encontrado:
        print("Produto não cadastrado")