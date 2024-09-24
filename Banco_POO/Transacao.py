from abc import ABC, ABCMeta, abstractmethod

class Transacao(ABC):

    @abstractmethod
    def registrar(self,conta):
        pass


class Deposito(Transacao):

    def __init__(self, valor):
        self.valor = valor

    def registrar(self,conta):
        conta.depositar(self.valor)


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


