salario = float(input())
if 0<= salario <= 400.00:
 percentual = 1.15
 
elif 400.01<= salario <= 800.00:
 percentual = 1.12
 
elif 800.01<= salario <= 1200.00:
 percentual = 1.10
 
elif 1200.01<= salario <= 2000.00:
 percentual = 1.07
else:
    percentual = 1.04
novosal = salario * percentual

print(f'Novo salario: {novosal:.2f}')
print(f'Reajuste ganho: {novosal - salario:.2f}')
if percentual == 1.15:
 print('Em percentual: 15 %')
elif percentual == 1.12:
 print('Em percentual: 12 %')
elif percentual == 1.10:
 print('Em percentual: 10 %')
elif percentual == 1.07:
 print('Em percentual: 7 %')
elif percentual == 1.04:
 print('Em percentual: 4 %')
