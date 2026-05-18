# Definição da classe que representa uma conta bancária simples
class contabancaria:
    def __init__(self):
        # Saldo inicial da conta é zero
        self.saldo_conta = 0
        
    def depositar(self):
        # Solicita ao usuário o valor do depósito
        valor_deposito = input('quanto sera o deposito:')
        # Converte a entrada em float e adiciona ao saldo
        self.saldo_conta += float(valor_deposito)
        print('deposito bem sucedido de ' + valor_deposito)

    def sacar(self):
        # Solicita ao usuário o valor do saque
        valor = int(input('digite o quanto quer sacar: '))
        # Verifica se há saldo suficiente antes de remover o valor
        if self.saldo_conta >= valor:
            self.saldo_conta -= valor
            print('saque bem sucedido')
        else:
            print('erro saldo indisponivel')

    def ver_extrato(self):
        # Exibe o saldo atual da conta com uma mensagem clara
        print(f'Saldo atual: R$ {self.saldo_conta}')



# Cria uma instância da conta bancária
conta = contabancaria()

# Loop principal do menu do sistema bancário
while True:
    print('menu de opçoes')
    print('1: depositar')
    print('2: sacar')
    print('3: ver extrato')
    print('4: sair do programa')
    opçoes = input('qual opçao: ')
    print(f"Opção escolhida: '{opçoes}'")  # Debug: mostra o que foi digitado

    # Executa a ação escolhida pelo usuário
    if opçoes == '1':
        conta.depositar()
    elif opçoes == '2':
        conta.sacar()
    elif opçoes == '3':
        conta.ver_extrato()
    elif opçoes == '4':
        print('saindo do programa')
        break
    else:
        # Se a opção não for válida, exibe mensagem de erro
        print('escolha uma opçao valida')






