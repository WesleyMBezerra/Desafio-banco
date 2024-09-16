from datetime import date

conta = 0

saques = {}

limiteSaque= 500

LIMITE_SAQUES = 3

contador = 0

usuario =[[],         #0:id 
          [],         #1:nome
          [],         #2:nascimento
          [],         #3:cpf
          [[],[]]]    #4:endereço => 0:cep, 1:numero

conta = [[],[]]

agencia = "0001"

contas = 1

def cadastrarUsuario():
    global contador
      
    print("___Cadastro Usuario___")

    contador += 1

    usuario[0].append(contador)

    nome = input("Digite seu nome: ")
    usuario[1].append(nome)

    data = input("Digite sua data de nascimento no formato 'dia-mês-ano: ")

    usuario[2].append(data)

    cpf = input("Digite apenas os números de seu CPF: ")

    if cpf in usuario[3] : 
        print("Esse CPF já foi cadastrado anteriormente")
        exit()

    else:
        usuario[3].append(cpf)
    
    endereco = input("Digite seu cep e o número da sua casa, utilizando apenas os números: ")

    endereco_dividido = endereco.split()

    usuario[4][0].append(endereco_dividido[0])
    usuario[4][1].append(endereco_dividido[1])

    

def contaBancaria():
    global contas
    cpf = input("Digite o CPF do usuário que deseja criar a conta: ")

    if cpf in usuario[3]:
        conta[0] = str(contas) +" " +  agencia
        conta[1] = cpf
        contas +=1

    else:
        print("O cpf digitado não foi cadastrado, crie uma conta para esse usuário: ")
        exit()


    print(conta)

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
        case "U":
            cadastrarUsuario()
        case "C":
            contaBancaria()
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
              "Cadastrar Usuário => U\n"
              "Criar Conta => C\n"
              "Sair => X\n")

        menu(entrada.upper())

        if entrada.upper() == "X": break
        


