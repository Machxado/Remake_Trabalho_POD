from abc import ABC, abstractmethod
from ClinicaSys.Error import *
from datetime import *


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
    
    @credito.setter
    def credito(self,credito):
        self.__credito = credito

    def __str__(self):
        return f'Convênio: {self.nome}, Crédito restante: R$ {self.credito}'



class Paciente(Pessoa):
    def __init__(self,nome,cpf,data_nascimento,est_civil,plano,credito):
        super().__init__(nome,cpf,data_nascimento,est_civil)
        self.__Pconvenio = Convenio(plano,credito)
        self.__diagnostico = None

    @property
    def Pconvenio(self):
        return self.__Pconvenio
    
    @property
    def diagnostico(self):
        return self.__diagnostico
    
    @diagnostico.setter
    def diagnostico(self,diagnostico):
        self.__diagnostico = diagnostico
    
    def cadastrarDados(self):
        pass

    def obterDados(self):
        return self.__str__()
    
    def __isub__(self, quantia):
        self.Pconvenio.credito -= quantia
        return self

    def __iadd__(self, quantia):
        self.Pconvenio.credito += quantia
        return self

    def __str__(self):
        return f'{super().__str__()}, {self.Pconvenio}'
    

    
class Medico(Pessoa):
    def __init__(self, nome,cpf,data_nascimento,est_civil,crm):
        super().__init__(nome,cpf,data_nascimento,est_civil)
        self.__crm = crm

    @property
    def crm(self):
        return self.__crm
    
    def diagnosticar(self,paciente:Paciente,diagnostico):
        if paciente.Pconvenio.credito < 150 and paciente.Pconvenio.nome != 'SUS':        
            print('O paciente não possui crédito suficiente para realizar o diagnóstico.')
        else:
            leitura = open('Saidas\\database\\pacientes.dat','r')
            texto=leitura.readlines()

            paciente -= 150
            paciente.diagnostico = diagnostico
            
            for i in range(0,len(texto)):
                if texto[i].split(',')[0] == 'Nome: '+paciente.nome:
                    parte1 = texto[i].split(sep=',')[0]+','+texto[i].split(sep=',')[1]+','+texto[i].split(sep=',')[2]+','+texto[i].split(sep=',')[3]
                    texto[i]= f'{parte1}, {paciente.Pconvenio}, Diagnóstico: {diagnostico}\n'
            
            escrita = open('Saidas\\database\\pacientes.dat','w')
            escrita.writelines(texto)
            leitura.close()
            escrita.close()

    def liberar(self,paciente:Paciente):
        leitura = open('Saidas\\database\\pacientes.dat','r')
        texto=leitura.readlines()
        
        for i in range(0,len(texto)):
            if texto[i].split(',')[0] == 'Nome: '+paciente.nome:
                parte1 = texto[i].split(sep=',')[0]+','+texto[i].split(sep=',')[1]+','+texto[i].split(sep=',')[2]+','+texto[i].split(sep=',')[3]
                texto[i]= f'{parte1}, {paciente.Pconvenio}, Liberado \n'
            
        escrita = open('Saidas\\database\\pacientes.dat','w')
        escrita.writelines(texto)
        leitura.close()
        escrita.close()

    def internar(self,paciente:Paciente):
        if paciente.Pconvenio.credito < 500 and paciente.Pconvenio.nome != 'SUS':
            print('O paciente não possui crédito suficiente para realizar a internação.')
        else:
            leitura = open('Saidas\\database\\pacientes.dat','r')
            texto=leitura.readlines()
            
            paciente -= 500

            for i in range(0,len(texto)):
                if texto[i].split(',')[0] == 'Nome: '+paciente.nome:
                    parte1 = texto[i].split(sep=',')[0]+','+texto[i].split(sep=',')[1]+','+texto[i].split(sep=',')[2]+','+texto[i].split(sep=',')[3]
                    texto[i]= f'{parte1}, {paciente.Pconvenio}, Internado\n'
                
            escrita = open('Saidas\\database\\pacientes.dat','w')
            escrita.writelines(texto)
            leitura.close()
            escrita.close()

    def obterDados(self):
        return self.__str__()
    
    def cadastrarDados(self):
        arq=open('Saidas\\database\\funcionarios.dat','a')
        arq.writelines(f'\n{self.obterDados()}')

    def __str__(self):
        return f'Cargo: Médico, {super().__str__()}, CRM: {self.crm}'
    


class Enfermeira(Pessoa):
    def __init__(self, nome,cpf,data_nascimento,est_civil,coren):
        super().__init__(nome,cpf,data_nascimento,est_civil)
        self.__coren = coren
    
    @property
    def coren(self):
        return self.__coren
    
    def obterDados(self):
        return self.__str__()
    
    def cadastrarDados(self):
        arq=open('Saidas\\database\\funcionarios.dat','a')
        arq.writelines(f'\n{self.obterDados()}')

    def cadastrarPaciente(self,paciente:Paciente):
        arq=open('Saidas\\database\\pacientes.dat','a')
        arq.writelines(f'\n{paciente.obterDados()}')

    def gerarRelatorio(self,medico:Medico,paciente:Paciente):
        dia = datetime.now().strftime('%d-%m-%Y')
        texto=f'''
===========================================
Relatório de atendimento Hospital São Lucas
===========================================
                                                Dia: {dia}
Relatamos que o paciente {paciente.nome}, proprietário do CPF: {paciente.cpf},
foi atendido pelo médico {medico.nome}, credenciado pelo CRM: {medico.crm},
o qual diagnosticou o paciente com {paciente.diagnostico}. 
Saldo final do convênio do paciente: {paciente.Pconvenio.credito}
        '''
        arq=open(f'Saidas/Relatorios/relatorio_{dia}_{paciente.cpf}','x')
        arq.writelines(texto)
    
    def __str__(self):
        return f'Cargo: Enfermeira, {super().__str__()}, COREN: {self.coren}'
    


class Secretaria(Pessoa):
    def __init__(self, nome,cpf,data_nascimento,est_civil):
        super().__init__(nome,cpf,data_nascimento,est_civil)
    
    def obterDados(self):
        return self.__str__()
    
    def cadastrarDados(self):
        arq=open('Saidas\\database\\funcionarios.dat','a')
        arq.writelines(f'\n{self.obterDados()}')
    
    def cadastrarFuncionarios(self,funcionario:Pessoa):
        match str(type(funcionario)):
            case '<class \'ClinicaSys.Classes.Medico\'>':
                try:
                    assert verifica_crm_existe(funcionario.crm,funcionario.nome)
                except AssertionError:
                    print('CRM já cadastrado')
                else: funcionario.cadastrarDados() 
            
            case '<class \'ClinicaSys.Classes.Enfermeira\'>':
                try:
                    assert verifica_coren_existe(funcionario.coren,funcionario.nome)
                except AssertionError:
                    print('COREN já cadastrado')
                else: funcionario.cadastrarDados() 

            case '<class \'ClinicaSys.Classes.Secretaria\'>':
                funcionario.cadastrarDados()
    
    def __str__(self):
        return f'Cargo: Secretária, {super().__str__()}'