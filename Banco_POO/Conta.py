class Conta(abc):

    
    def __init__(self,saldo:float, numero:int,agencia:str = "0001") -> Conta :
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente: Cliente = Cliente()
        self.historico: Historico = Historico()