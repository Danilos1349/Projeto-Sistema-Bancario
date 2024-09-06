menu = '''

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


while True:

    opcao = input(f'Seja bem vindo! Qual operação gostaria de fazer: {menu}')


    if opcao == 'd':
        print('Depósito', end='\n\n')
        valor_depositado = float(input('Digite o valor que será depositado: '))
        
        if valor_depositado <= 0:
            print('Valor inválido! Digite um valor acima de 0 reais.')
        else:
            print(f'Seu depósito de R$ {valor_depositado:.2f} foi efetuado com sucesso.')
            saldo += valor_depositado
            extrato += f'Depósito: R$ {valor_depositado:.2f}\n'        


    elif opcao == 's':
        print('Saque', end='\n\n')

        if numero_de_saques < LIMITES_DE_SAQUES:
            valor_sacado = float(input('Digite o valor que você deseja sacar: '))

            if valor_sacado <= 0:
                print('Valor inválido. Seu valor deve ser maior do que R$ 0.00')
            
            elif valor_sacado > limite:
                print(f'Você excedeu a quantia máxima por saque. Seu limite é de R$ {limite:.2f}')

            elif valor_sacado > saldo:
                print('Saldo insuficiente para realizar esta operação.')
            
            else:
                print(f'Você fez um saque de R$ {valor_sacado:.2f}')
                saldo -= valor_sacado
                extrato += f'Saque: R$ {valor_sacado:.2f}\n'
                numero_de_saques += 1
        
        else:
            print('Você atingiu o limite de saques diários.')


    elif opcao == 'e':
        print('Extrato', end='\n\n')
        print("************* EXTRATO *************")
        if extrato == '':
            print('Não foram realizadas movimentações nessa conta')
        else:
            print(extrato)
            print(f'Seu saldo atual é de R$ {saldo:.2f}')
        print("***********************************")

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione uma opção válida')