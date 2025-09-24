class Fila:
    def __init__(self):
        self.fila = []

    def enfileirar(self, elemento):
        self.fila.append(elemento)
        print(f"Elemento '{elemento}' inserido no final da fila.")

    def desenfileirar(self):
        if self.fila:
            elemento = self.fila.pop(0)
            print(f"Elemento '{elemento}' removido do início da fila.")
        else:
            print("A fila está vazia. Nenhum elemento para remover.")

    def consultar(self):
        if self.fila:
            print(f"O elemento no início da fila é: '{self.fila[0]}'")
        else:
            print("A fila está vazia. Nenhum elemento para consultar.")

    def contar(self):
        print(f"A quantidade de elementos na fila é: {len(self.fila)}")


def menu():
    print("\n----- Menu de Opções -----")
    print("1 - Enfileirar")
    print("2 - Desenfileirar")
    print("3 - Consultar")
    print("4 - Contar")
    print("5 - Sair")


fila = Fila()

while True:
    menu()
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '1':
        elemento = input("Digite o elemento para enfileirar: ")
        fila.enfileirar(elemento)

    elif opcao == '2':
        fila.desenfileirar()

    elif opcao == '3':
        fila.consultar()

    elif opcao == '4':
        fila.contar()

    elif opcao == '5':
        print("Programa Finalizado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
