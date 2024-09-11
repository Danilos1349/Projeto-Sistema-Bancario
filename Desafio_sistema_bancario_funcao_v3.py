from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacoes(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

     
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        self._saldo

    @property
    def numero(self):
        self._numero

    @property
    def agencia(self):
        self._agencia

    @property
    def cliente(self):
        self._cliente

    @property
    def historico(self):
        self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('ERRO NA OPERAÇÃO', 'Saldo insuficiente para realizar esta operação.', sep='\n')

        elif valor > 0:
            self.saldo -= valor
            print(f'Você fez um saque de R$ {valor:.2f}')
            return True

        else:
            print('ERRO NA OPERAÇÃO', 'Valor inválido. Seu valor deve ser maior do que R$ 0.00', sep='\n')
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Seu depósito de R$ {valor:.2f} foi efetuado com sucesso.')
        else:
            print('ERRO NA OPERAÇÃO', 'Valor inválido! Digite um valor acima de 0 reais.', sep='\n')
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, numero_saques=3, limite=500):
        super().__init__(numero, cliente)
        self.numero_saques = numero_saques
        self.limite = limite

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques > self.numero_saques

        if excedeu_limite:
            print('ERRO NA OPERAÇÃO', 
              f'Você excedeu a quantia máxima por saque. Seu limite é de R$ {self.limite:.2f}', sep='\n')
            
        elif excedeu_saques:
            print('\nVocê atingiu o limite de saques diários.')

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    
class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(cls, conta) -> None:
        pass    

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)










