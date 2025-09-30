class Conta:
    numero: int = 35017
    saldo: float = 15.000
    tipo: str = 'Salário'

    def __init__(self, numero, saldoInicial):
        self.numero = numero
        self.saldo = saldoInicial

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if (self.saldo > 0):
            self.saldo -= valor
        else:
            print('ta pobre')
#main
conta = Conta('3501-7', 10000)
print(conta.numero)
print(conta.saldo)
