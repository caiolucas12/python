quantidade = 0
soma = 0
for i in range(6):
    valor = float(input())
    if valor > 0:
        soma = soma + valor
        quantidade = quantidade + 1

print(quantidade, 'valores positivos')
print(f'{soma/quantidade:.1f}')