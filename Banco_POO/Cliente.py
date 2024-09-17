from abc import ABC, classmethod, abstractmethod
from datetime import datetime

class cliente(ABC):

    def __init__(self,endereco:str,contas: list):
        self.endereco = endereco
        self.contas = contas

    def realizar_transacao(conta: Conta, transacao:Transacao):

        pass

    def adicionar_conta(conta: Conta):

        pass

    
class PessoaFisica(cliente):

    def __init__(self, endereco: str, contas: list, cpf: str, nome:str,nascimento:date):
        super().__init__(endereco, contas)
        self.cpf =cpf