from abc import ABC, classmethod, abstractmethod
import random 

class Conta(ABC):

    
    def __init__(self,saldo:float, numero:int,agencia:str = "-0001") -> Conta :
        self.saldo = saldo
        self.numero = str(random.randint(1,999))
        self.agencia = agencia
        self.cliente: Cliente = Cliente()
        self.historico: Historico = Historico()


    def saldo()->float:
        return self.saldo
    
    def nova_conta(numero:int)-> Conta:
        pass

    def sacar(valor:float)->bool:

        pass

    def depositar(valor:float)->bool:

        pass

class ContaCorrente(Conta):

    def __init__(self, saldo: float, numero: int, agencia: str = "0001" ):
        super().__init__(saldo, numero, agencia)
        self.limite = 5000
        self.limite_saques = 5


