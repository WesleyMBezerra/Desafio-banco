from Conta import ContaCorrente
from Transacao import Saque, Deposito
from Cliente import PessoaFisica

# Criando cliente
cliente1 = PessoaFisica(endereco="Rua A", cpf="12345678901", nome="João", nascimento="1990-01-01")

# Criando conta corrente para o cliente
conta1 = ContaCorrente(saldo=1000, Cliente=cliente1)
cliente1.adicionar_conta(conta1)

# Realizando transações
deposito = Deposito(300)
cliente1.realizar_transacao(conta1, deposito)  # Depósito de 300

saque = Saque(200)
cliente1.realizar_transacao(conta1, saque)     # Saque de 200

# Verificando saldo
print(f"Saldo atual: {conta1.saldo}")

# Exibindo o histórico
print(f"Histórico de transações: {conta1.historico.transacoes}")
