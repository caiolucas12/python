class Conta:
    numero: int = 35017
    saldo: float = 15.000
    tipo: str = 'Salário'
banco = Conta()   #ou banco = Conta

banco.numero
banco.saldo
print(f'Número: {banco.numero}')
print(f'Saldo: {banco.saldo}')
print(f'Tipo: {banco.tipo}')