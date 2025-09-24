import random

lista_a_ser_preenchida = [random.randint(0, 1000) for _ in range(100)]

lista_pares = []
lista_impares = []

for num in lista_a_ser_preenchida:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print("Lista com 100 números inteiros:")
print(lista_a_ser_preenchida)

print("\nLista dos números pares:")
print(lista_pares)

print("\nLista dos números ímpares:")
print(lista_impares)
