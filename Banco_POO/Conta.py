from abc import ABC
import random 
from Transacao import Historico

class Conta(ABC):

    def __init__(self,saldo:float,Cliente):
        self._saldo = saldo
        self.numero = str(random.randint(1,999))
        self.agencia = "-0001"
        self.cliente = Cliente
        self.historico: Historico = Historico()

    @property
    def saldo(self)->float:
        return self._saldo
    
    def sacar(self, valor:float)->bool:
        if valor > self._saldo:
            print(f"Saque de {valor} falhou: saldo insuficiente.")
            return False
        self._saldo -= valor
        self.historico.adicionar_transacao(f"Saque de {valor}")
        return True

    def depositar(self,valor:float)->bool:
        self._saldo += valor
        self.historico.adicionar_transacao(f"Depósito de {valor}")
        return True

class ContaCorrente(Conta):

    def __init__(self, saldo: float, Cliente):
        super().__init__(saldo, Cliente)
        self.limite = 5000
        self.limite_saques = 5
        self.saques_realizados = 0


    def sacar(self, valor)-> bool:
        if self.saques_realizados >= self.limite_saques:
            print(f"Limite de saques excedido.")
            return False
        if valor > (self._saldo + self.limite):
            print(f"Saque de {valor} falhou: limite insuficiente.")
            return False
        self._saldo -= valor
        self.saques_realizados += 1
        self.historico.adicionar_transacao(f"Saque de {valor}")
        return True


