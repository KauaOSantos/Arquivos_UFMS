tempo = float(input("Digite o tempo da viagem em horas: "))
velocidade_media = float(input("Digite a velocidade média em km/h: "))
consumo_medio = float(input("Digite o consumo médio do veículo em km/l: "))

distancia = tempo * velocidade_media
combustivel_gasto = distancia / consumo_medio

print(f"A quantidade de combustível gasto foi de {combustivel_gasto:.2f} litros.")