class Conta:
    def __init__(self, numero_agencia, saldo=0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia
    
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self._saldo -= valor
    
    def mostrar_saldo(self): #forma certa de mostrar o saldo
        return self._saldo


conta = Conta('0001', 100)
conta.depositar(100)
print(conta._saldo) # forma errada de mostrar o saldo!!
print(conta.numero_agencia)
print(conta.mostrar_saldo()) #forma certa de mostrar o saldo