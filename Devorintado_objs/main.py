class Main:
    pass

print('Testando projeto')

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João", "114444-2222")
conta=Conta(c1.get_nome(), 1222)

conta.deposito(100)
conta.saque(50)
conta.extrato()