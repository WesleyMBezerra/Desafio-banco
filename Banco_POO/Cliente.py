from abc import ABC
from datetime import datetime, date
from Conta import Conta
from Transacao import Transacao


class cliente(ABC):

    def __init__(self,endereco:str):
        self.endereco = endereco
        self.contas = []
        

    def realizar_transacao(self, conta: Conta, transacao:Transacao):
        if conta in self.contas:
            transacao.registrar(conta)
        else:
            print("Conta não encontrada para o cliente.")


    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)
        pass

    
class PessoaFisica(cliente):

    def __init__(self, endereco: str, cpf: str, nome:str,nascimento:date):
        super().__init__(endereco)
        self.cpf =cpf
        self.nome = nome
        self.nascimento = nascimento


