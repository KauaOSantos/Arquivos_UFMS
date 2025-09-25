def funcao_recursiva(numero):
    if (numero <= 0):
        return 0
    else:
        return numero + funcao_recursiva(numero - 1)
    
numero = int(input("Digite um número: "))
funcao = funcao_recursiva(numero)
print(f'Resultado da soma dos números anteriores: {funcao}')