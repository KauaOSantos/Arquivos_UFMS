quantidade = int(input("Digite a quantidade de produtos que deseja cadastrar: "))
produtos = []

for _ in range(quantidade):
    produto = input("Digite o nome do produto: ").strip()
    preco = float(input(f"Digite o preço do produto {produto}: "))

    produtoCadastrado = False

    for item in produtos:
        if item[0] == produto: 
            print("Produto já cadastrado")  
            produtoCadastrado = True  
            break  

    if not produtoCadastrado:
        produtos.append((produto, preco))  

while True:
    produtoBuscado = input("Digite o nome do produto para busca ou 'Fim' para encerrar: ").strip()
    if produtoBuscado == "Fim":  
        break  

    encontrado = False

    for item in produtos:
        if item[0] == produtoBuscado:  
            print(f"Preço do produto '{produtoBuscado}': R$ {item[1]:.2f}")  
            encontrado = True  
            break 

    if not encontrado:
        print("Produto não cadastrado")