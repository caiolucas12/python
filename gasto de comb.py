consumo_medio = 12
tempo = int(input('Tempo da viagem (hora): '))
vmed = int(input('Velocidade Média(km/h): '))

distancia = vmed * tempo

gasto = distancia / consumo_medio
print(f'{gasto:.3f}')
