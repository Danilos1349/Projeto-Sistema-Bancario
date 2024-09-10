menu = '''
Seja bem vindo!
Seleciona a operação que gostaria de realizar:

[d] Depositar
[s] Saque
[e] Extrato
[c] Cadastrar Cliente
[a] Criar Conta
[m] Mostrar Contas
[q] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITES_DE_SAQUES = 3
banco_dados_clientes = []
cpf_clientes = set()
contas = []
AGENCIA = '0001'
numero_conta = 0

# funcão depósito
def depositar(saldo, extrato, valor_depositado, /):

    if valor_depositado <= 0:
        print('ERRO NA OPERAÇÃO', 'Valor inválido! Digite um valor acima de 0 reais.', sep='\n')
        return saldo, extrato
    
    else:
        print(f'Seu depósito de R$ {valor_depositado:.2f} foi efetuado com sucesso.')
        saldo += valor_depositado
        extrato += f'Depósito: R$ {valor_depositado:.2f}\n'    
        return saldo, extrato

# função saque
def sacar(*, saldo, extrato, numero_de_saques,limite, valor_sacado):

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
def mostrar_extrato(saldo, /, *, extrato):
    
    print("************* EXTRATO *************")
    if extrato == '':
        print('Não foram realizadas movimentações nessa conta')
    else:
        print(extrato)
        print(f'Seu saldo atual é de R$ {saldo:.2f}')
    print("***********************************")

# função cadastrar cliente

def cadastrar_cliente(nome, nascimento, cpf, endereco):
    
    cpf_clientes.add(cpf)
    banco_dados_clientes.append(dict(nome=nome, nascimento=nascimento,cpf=cpf,endereco=endereco))
    

def filtrar_cliente(cpf, banco_dados_clientes):
    for cliente in banco_dados_clientes:
        if cliente['cpf'] == cpf:
            return cliente

def criar_conta(AGENCIA, numero_conta, banco_dados_clientes, contas):
    cpf = input('Digite o CPF do clientes: ')
    usuario = filtrar_cliente(cpf, banco_dados_clientes)

    if usuario:
        numero_conta += 1
        conta = {'agencia': AGENCIA, 'numero_conta': numero_conta, 'usuario': usuario}
        contas.append(conta)
        return conta, numero_conta
    
    else:
        print('Usuário não localizado. Verifique se o CPF já está cadastrado.')
        return None, numero_conta


def mostrar_contas(contas):
    if contas:
        print("\n********** CONTAS CADASTRADAS **********\n")
        for conta in contas:
            print(f'Agência: {conta["agencia"]}', f'Número da Conta: {conta["numero_conta"]}', f"Cliente: {conta["usuario"]["nome"]}", sep='\n')
            print("\n****************************************\n")
    else:
        print("Nenhuma conta cadastrada.")

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor_depositado = float(input('\nDigite o valor que será depositado: '))
        saldo, extrato = depositar(saldo, extrato, valor_depositado)

    elif opcao == 's':
        if numero_de_saques < LIMITES_DE_SAQUES:
            valor_sacado = float(input('\nDigite o valor que você deseja sacar: '))
            saldo, extrato, numero_de_saques = sacar(saldo=saldo, extrato=extrato, 
                                                     numero_de_saques=numero_de_saques, limite=limite, 
                                                     valor_sacado=valor_sacado)
            
        else:
            print('\nVocê atingiu o limite de saques diários.')

    elif opcao == 'e':
        mostrar_extrato(saldo, extrato=extrato)

    elif opcao == 'c':
            cpf_cliente = input('Digite o CPF (somente números): ')
            if cpf_cliente in cpf_clientes:
                print('ERRO! Número de CPF já cadastrado')
                continue 
            else:
                nome_cliente = input('Digite o nome completo do cliente: ')
                data_nascimento = input('Digite a data de nascimento (dia/mês/ano): ')
                logradouro_cliente = input('Digite o logradouro: ')
                numero_casa_cliente = input('Digite o número da casa/prédio: ')
                bairro_cliente = input('Digite o nome do bairro: ')
                cidade_cliente = input('Digite o nome da cidade: ')
                estado_cliente = input('Digite a sigla do estado: ')
                endereco_cliente = f'{logradouro_cliente}, {numero_casa_cliente} - {bairro_cliente} - {cidade_cliente}/{estado_cliente}'

            cadastrar_cliente(nome=nome_cliente, nascimento=data_nascimento, cpf=cpf_cliente, endereco=endereco_cliente)
            print('\nCliente cadastrado com sucesso!')

    elif opcao == 'a':
        conta, numero_conta = criar_conta(AGENCIA, numero_conta, banco_dados_clientes, contas)
        if conta:
            print(f'Conta criada com sucesso! Número da conta: {numero_conta}')

    elif opcao == 'm':
        mostrar_contas(contas)    

    elif opcao == 'q':
        print('\nObrigado por utilizar nossos serviços.', 
              'É um prazer ter você como cliente.', 'Tenha um ótimo dia! ', sep='\n')
        break

    else:
        print('\nERRO NA OPERAÇÃO', 'Digite uma opção válida', sep='\n')