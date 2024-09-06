menu = '''
Seja bem vindo!
Seleciona a operação que gostaria de realizar:

[d] Depositar
[s] Saque
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITES_DE_SAQUES = 3

# funcão depósito
def deposito(saldo, extrato, valor_depositado):

    if valor_depositado <= 0:
        print('ERRO NA OPERAÇÃO', 'Valor inválido! Digite um valor acima de 0 reais.', sep='\n')
        return saldo, extrato
    
    else:
        print(f'Seu depósito de R$ {valor_depositado:.2f} foi efetuado com sucesso.')
        saldo += valor_depositado
        extrato += f'Depósito: R$ {valor_depositado:.2f}\n'    
        return saldo, extrato

# função saque
def saque(saldo, extrato, numero_de_saques,limite, valor_sacado):

    if valor_sacado <= 0:
        print('ERRO NA OPERAÇÃO', 'Valor inválido. Seu valor deve ser maior do que R$ 0.00', sep='\n')
        return saldo, extrato, numero_de_saques
            
    elif valor_sacado > limite:
        print('ERRO NA OPERAÇÃO', 
              f'Você excedeu a quantia máxima por saque. Seu limite é de R$ {limite:.2f}', sep='\n')
        return saldo, extrato, numero_de_saques

    elif valor_sacado > saldo:
        print('ERRO NA OPERAÇÃO', 'Saldo insuficiente para realizar esta operação.', sep='\n')
        return saldo, extrato, numero_de_saques
    
    else:
        print(f'Você fez um saque de R$ {valor_sacado:.2f}')
        saldo -= valor_sacado
        extrato += f'Saque: R$ {valor_sacado:.2f}\n'
        numero_de_saques += 1
        return saldo, extrato, numero_de_saques

# funcão extrato
def mostrar_extrato(extrato, saldo):
    
    print("************* EXTRATO *************")
    if extrato == '':
        print('Não foram realizadas movimentações nessa conta')
    else:
        print(extrato)
        print(f'Seu saldo atual é de R$ {saldo:.2f}')
    print("***********************************")

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor_depositado = float(input('\nDigite o valor que será depositado: '))
        saldo, extrato = deposito(saldo, extrato, valor_depositado)

    elif opcao == 's':
        if numero_de_saques < LIMITES_DE_SAQUES:
            valor_sacado = float(input('\nDigite o valor que você deseja sacar: '))
            saldo, extrato, numero_de_saques = saque(saldo, extrato, numero_de_saques, limite, valor_sacado)
        else:
            print('\nVocê atingiu o limite de saques diários.')

    elif opcao == 'e':
        mostrar_extrato(extrato, saldo)

    elif opcao == 'q':
        print('\nObrigado por utilizar nossos serviços.', 
              'É um prazer ter você como cliente.', 'Tenha um ótimo dia! ', sep='\n')
        break

    else:
        print('\nERRO NA OPERAÇÃO', 'Digite uma opção válida', sep='\n')