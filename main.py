
conta = 0

saques = {}

limiteSaque= 500

LIMITE_SAQUES = 3

def deposito(valor: float):
    if(valor <= 0):
        print(f"\nO valor do deposito não pode ser R${valor}, deve ser um valor positivo ")
    else:
        global conta 
        conta += valor
        print("\nValor em conta  R$", conta)


        

def saque(valor: float):
    global conta
    global LIMITE_SAQUES
    if (LIMITE_SAQUES == 0):
        print("\nNão é possível realizar mais saques")      
    else:
        if(valor > conta):
            print(f"\nNão é possível realizar o saque de {valor}")
        else:
            LIMITE_SAQUES -= 1
            saques[LIMITE_SAQUES] = valor
            conta -= valor
            print(f"\nSeu saque de R${valor} foi realizado com sucesso\n"
                  f"Você ainda possui {LIMITE_SAQUES} disponíveis")
            
    

def extrato():
    contadorSaques = 0
    if(len(saques) == 0):
        print("\nNão foram realizadas movimentações")
    else:
        print(f"\nExtrato da conta: \n")
        for saque in saques:
            contadorSaques+=1
            print("Número: ",contadorSaques,"Valor:", saques[saque])
        print(f"conta :R$:{conta}")


def menu(entrada: str):
    match entrada:
        case "D":
            valor = float(input("Insira um valor de deposito: "))
            deposito(valor)
        case "S":
            valor = float(input("Insira um valor de saque: "))
            saque(valor)
        case "E":
            extrato()
        case "X":
            print("Encerrando...")
        case _:
            print("Insira uma entrada válida")


if __name__ == "__main__":

    while(True):

        print("\n__MENU DO BANCO__")
        entrada =input("Selecione uma das opções para realizar uma operação\n"
              "Depositar => D\n"
              "Saque => S\n"
              "Extrato => E\n"
              "Sair => X\n")

        menu(entrada.upper())

        if entrada.upper() == "X": break
        


