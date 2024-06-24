
from abc import ABC, abstractmethod

from datetime import datetime

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property  
    def saldo(self):
        return self._saldo    

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @property
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou, saldo insuficiente!")

        elif valor > 0:
            saldo -= valor
            print("Saque efetuado com sucesso!")
            return True

        else:
            print("Operação falhou, por favor informe um valor válido")

        return False
    
    @property
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")

        else:
            print("Operação falhou, o valor informado não é válido")
            return False
        
        return True
        

class conta_corrente(Conta):

    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transaçao for transaçao in self.historico.trasaçoes if transaçao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self.limite
        execedeu_saques = numero_saques >= self.limite_saques

        


class Cliente:
    def __init__(self, endereço, contas):
        self.endereço = endereço
        self.contas = []

    def realizar_trasaçao(self, contas, transaçao):
        transaçao.registrar(contas)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    

class PessoaFisica(Cliente):
    
    def __init__(self, cpf, nome, data_nascimento, endereço):
        super().__init__(endereço)
        self.cpf  = cpf 
        self.nome = nome
        self.data_nascimento = data_nascimento

   


class Transaçao(ABC):
    
    def registrar(self):
        pass

class Deposito(Transaçao):
    pass

class Saque(Transaçao):
    pass

class Historico:
    
    def adicionar_transaçao(self):
        pass