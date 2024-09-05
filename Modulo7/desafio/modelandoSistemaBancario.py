
from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass
    
    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        conta.depositar(self._valor)
        conta.historico.adicionar_transacao(self)
    pass

class Saque(Transacao):
    def __init__(self, valor) -> None:
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        conta.sacar(self._valor)
        conta.historico.adicionar_transacao(self)

    

class Cliente():

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:

    def __init__(self, numero, cliente,agencia="0001", saldo=0, historico = Historico() ):
        self._numero = numero
        self._cliente = cliente
        self._agencia = agencia
        self._saldo = saldo
        self._historico = historico

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    def sacar(self, valor):
        print(f"Valor de {valor} sacado.")

    def depositar(self, valor):
        print(f"Valor de {valor} depositado")

class ContaCorrente(Conta):

    def __init__(self, numero, cliente,limite, limite_saques, agencia="0001", saldo=0,  historico=Historico()):
        super().__init__(numero, cliente, agencia, saldo, historico)
        self.limite = limite
        self.limite_saques = limite_saques

class Historico():
    def __init__(self) -> None:
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)