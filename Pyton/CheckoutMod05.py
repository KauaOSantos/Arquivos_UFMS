'''Este programa realiza o cadastro de produtos e seus preços,
verifica duplicidade durante o cadastro e permite buscar preços dos produtos cadastrados.
O programa continua até que o usuário digite "Fim" ao buscar produtos.
'''
# Solicita ao usuário a quantidade de produtos a serem cadastrados
quantidade = int(input("Digite a quantidade de produtos que deseja cadastrar: "))
# Inicializa uma lista vazia para armazenar os produtos e seus respectivos preços
produtos = []

# Laço para cadastrar os produtos e preços
for _ in range(quantidade):
    # Solicita o nome do produto, removendo espaços em branco nas extremidades
    produto = input("Digite o nome do produto: ").strip()
    # Solicita o preço do produto e converte para tipo float
    preco = float(input(f"Digite o preço do produto {produto}: "))

    # Variável de controle para verificar duplicidade do produto
    produtoCadastrado = False

    # Laço para verificar se o produto já está cadastrado na lista
    for item in produtos:
        if item[0] == produto:  # item[0] é o nome do produto na tupla
            print("Produto já cadastrado")  # Mensagem de alerta
            produtoCadastrado = True  # Marca como duplicado
            break  # Encerra a verificação para este produto

    # Se o produto não foi cadastrado, adiciona à lista de produtos
    if not produtoCadastrado:
        produtos.append((produto, preco))  # Adiciona uma tupla (produto, preco)

# Laço infinito para realizar buscas de preços de produtos
while True:
    # Solicita ao usuário o nome do produto a ser buscado
    produtoBuscado = input("Digite o nome do produto para busca ou 'Fim' para encerrar: ").strip()
    if produtoBuscado == "Fim":  # Verifica se o usuário quer encerrar o programa
        break  # Sai do laço infinito

    # Variável de controle para verificar se o produto foi encontrado
    encontrado = False

    # Laço para buscar o produto na lista de produtos
    for item in produtos:
        if item[0] == produtoBuscado:  # Compara o nome do produto buscado com o nome na lista
            print(f"Preço do produto '{produtoBuscado}': R$ {item[1]:.2f}")  # Exibe o preço
            encontrado = True  # Marca como encontrado
            break  # Encerra a busca para este produto

    # Se o produto não foi encontrado na lista, exibe mensagem de alerta
    if not encontrado:
        print("Produto não cadastrado")
'''
Comentários gerais sobre o código:
1. O programa utiliza uma lista para armazenar os produtos como tuplas (nome, preço).
2. Durante o cadastro, verifica-se a duplicidade para evitar conflitos nos dados.
3. O laço infinito para busca só encerra quando o usuário digita "Fim".
4. Tanto o nome do produto quanto a busca são tratados com .strip() para evitar erros causados por espaços em branco.
5. A estrutura é simples, mas pode ser ampliada para incluir funcionalidades como edição ou remoção de produtos.
'''
'''
Exemplo de execução:
Digite a quantidade de produtos que deseja cadastrar: 2
Digite o nome do produto: Maçã
Digite o preço do produto Maçã: 3.5
Digite o nome do produto: Laranja
Digite o preço do produto Laranja: 2.8
Digite o nome do produto para busca ou 'Fim' para encerrar: Maçã
Preço do produto 'Maçã': R$ 3.50
Digite o nome do produto para busca ou 'Fim' para encerrar: Uva
Produto não cadastrado
Digite o nome do produto para busca ou 'Fim' para encerrar: Fim
'''