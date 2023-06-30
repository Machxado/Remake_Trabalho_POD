from abc import ABC, abstractmethod
from ClinicaSys.Error import *


class Pessoa(ABC):
    def __init__(self, nome,cpf,data_nascimento,est_civil):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
        self.__est_civil = est_civil
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @property
    def est_civil(self):
        return self.__est_civil
    
    @abstractmethod
    def cadastrarDados(self):pass

    @abstractmethod
    def obterDados(self):pass

    

    def __str__(self):
        return f'Nome: {self.nome} proprietário do CPF {self.cpf} nascido em {self.data_nascimento} atualmente {self.est_civil}'



class Convenio():
    def __init__(self,nome,credito):
        assert(nome == 'Unimed' or nome == 'SUS' or nome == 'IPE'), print(ConvenioInvalido)
        self.__nome = nome
        assert(isinstance(credito,int))
        self.__credito = credito
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def credito(self):
        return self.__credito
    
    def __isub__(self, quantia):
        self.__credito -= quantia

    def __iadd(self, quantia):
        self.__credito += quantia

    def __str__(self):
        return f'{self.nome}, Crédito restante: R$ {self.credito}'



class Paciente(Pessoa):
    def __init__(self,nome,cpf,data_nascimento,est_civil,plano,credito):
        super().__init__(nome,cpf,data_nascimento,est_civil)
        self.__Pconvenio = Convenio(plano,credito)

    @property
    def Pconvenio(self):
        return str(self.__Pconvenio)
    
    def cadastrarDados(self):
        print('oi cadastrado')

    def obterDados(self):
        print('oi obtido')

    def __str__(self):
        return f'{super().__str__()}, possui o Convênio {self.Pconvenio}'