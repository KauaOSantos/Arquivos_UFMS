import random

print("Adivinhe o número secreto entre 0 e 10!")

numero_secreto = random.randint(0, 10)
tentativas = 0 

while True:
    try:
        numero_digitado = int(input("Digite o número que acha que é: "))
        tentativas += 1

        if numero_digitado == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.\n")
            break
        elif numero_digitado < numero_secreto:
            print("Muito baixo. Tente um número maior.\n")
        else:
            print("Tente um número menor.\n")
    except ValueError:
        print("Por Favor, digite um número inteiro.")