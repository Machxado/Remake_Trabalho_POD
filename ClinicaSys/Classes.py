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
        return f'Nome: {self.nome}, CPF: {self.cpf}, Data Nascimento: {self.data_nascimento}, Estado Cívil: {self.est_civil}'



class Convenio():
    def __init__(self,nome,credito):
        self.__nome = nome
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
        arq=open('Saidas\\database\\pacientes.dat','a')
        arq.writelines(f'\n{self.obterDados()}')

    def obterDados(self):
        return self.__str__()

    def __str__(self):
        return f'{super().__str__()}, Convênio: {self.Pconvenio}'
    

    
class Medico(Pessoa):
    def __init__(self, nome,cpf,data_nascimento,est_civil,crm):
        super().__init__(nome,cpf,data_nascimento,est_civil)
        self.__crm = crm

    @property
    def crm(self):
        return self.__crm
    
    def diagnosticar(self,paciente,diagnostico):
        leitura = open('Saidas\\database\\pacientes.dat','r')
        texto=leitura.readlines()
        
        for i in range(0,len(texto)):
            print(texto[i])
            if texto[i].split(',')[0] == 'Nome: '+paciente.nome:
                texto[i]=texto[i][0:-1]+f', Diagnóstico: {diagnostico}\n'
        
        escrita = open('Saidas\\database\\pacientes.dat','w')
        escrita.writelines(texto)
        leitura.close()
        escrita.close()

    def liberar(self):
        pass

    def internar(self):
        pass
    
    def obterDados(self):
        return self.__str__()
    
    def cadastrarDados(self):
        arq=open('Saidas\\database\\funcionarios.dat','a')
        arq.writelines(f'\n{self.obterDados()}')

    def __str__(self):
        return f'Cargo: Médico, {super().__str__()}, CRM: {self.crm}'