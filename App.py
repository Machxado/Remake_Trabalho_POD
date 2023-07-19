from ClinicaSys import Classes as cls
from ClinicaSys.Error import *

#abrindo arquivo txt e garantia de que haverá arquivo
for dia in range(1,6):
    
    print(f'DIA : {dia} ')
    arqname=str(dia)+'.txt'
    arq='Operacoes\\'+arqname

    try: 
        a = open(arq,'r')
    except FileNotFoundError:
        print(ArquivoNotFound(arqname))

    comandos = a.readlines()
    a.close()

    #removendo o \n
    for i in range(0,len(comandos)):
        comandos[i] = comandos[i][:-1]

    pacientes=[]


    #criação dos objetos
    for i in comandos:
        match i [0:2]:

            case  'Pa':

                nome = i.split(sep=':')[0][11:]
                cpf = i.split(sep=':')[1]
                data_nasc = i.split(sep=':')[2]
                est_civil = i.split(sep=':')[3]
                plano = i.split(sep=':')[4]
                credito = i.split(sep=':')[5]
                if(verifica_cpf(cpf,nome) and verifica_convenio(plano, nome) and verifica_data(data_nasc,nome) and verifica_est_civil(est_civil,nome) and verifica_credito(credito,nome)):
                    pacientes.append(cls.Paciente(nome,cpf,data_nasc,est_civil,plano,int(credito)))

            case 'Me':                
                if len(i.split(':')) <= 2:
                    try:
                        assert str(type(medico)) == '<class \'ClinicaSys.Classes.Medico\'>'
                    except Exception:
                        log_obj_n_existe('Medico',i.split(sep='=')[1].split(sep='->')[0])

                    match i.split(sep='=')[1].split(sep='->')[0]:

                        case 'internar':
                            npaciente=int(i.split(sep='->')[1][-1])-1
                            try:
                                medico.internar(pacientes[npaciente])
                            except IndexError:
                                log_obj_n_existe('pcaiente2','internar')

                        case 'liberar':
                            npaciente= int(i.split(sep='->')[1][-1])-1
                            try:
                                medico.liberar(pacientes[npaciente])
                            except IndexError:
                                log_obj_n_existe('pcaiente2','liberar')

                        case 'diagnosticar':
                            npaciente= int(i.split(sep='->')[1].split(sep=':')[0][-1])-1
                            try:
                                medico.diagnosticar(pacientes[npaciente],i.split(sep=':')[1])
                            except IndexError:
                                log_obj_n_existe('pcaiente2','diagnosticar')
                else: 

                    nome = i.split(sep=':')[0][8:]
                    cpf = i.split(sep=':')[1]
                    data_nasc = i.split(sep=':')[2]
                    est_civil = i.split(sep=':')[3]
                    crm = i.split(sep=':')[4][4:]
                    if(verifica_cpf(cpf,nome) and verifica_data(data_nasc,nome) and verifica_est_civil(est_civil,nome)):
                        medico=cls.Medico(nome,cpf,data_nasc,est_civil,crm)
                    
            case 'En':
                if len(i.split(':')) <= 2:
                    try:
                        assert str(type(enfermeira)) == '<class \'ClinicaSys.Classes.Enfermeira\'>'
                    except Exception:
                        log_obj_n_existe('Enfermeira',i.split(sep='=')[1].split(sep='->')[0])

                    match i.split(sep='=')[1].split(sep='->')[0]:
                        case 'cadastrar':
                            npaciente=int(i.split(sep='->')[1][-1])-1
                            try:
                                enfermeira.cadastrarPaciente(pacientes[npaciente])
                            except IndexError:
                                log_obj_n_existe('pcaiente2','cadastrar')

                        case 'relatorio':
                            npaciente=int(i.split(sep='->')[1][-1])-1
                            try:
                                enfermeira.gerarRelatorio(medico,pacientes[npaciente])
                            except IndexError:
                                log_obj_n_existe('pcaiente2','relatorio')
                
                else:
                    nome = i.split(sep=':')[0][12:]
                    cpf = i.split(sep=':')[1]
                    data_nasc = i.split(sep=':')[2]
                    est_civil = i.split(sep=':')[3]
                    coren = i.split(sep=':')[4]
                    if(verifica_cpf(cpf,nome) and verifica_data(data_nasc,nome) and verifica_est_civil(est_civil,nome)):
                        enfermeira=cls.Enfermeira(nome,cpf,data_nasc,est_civil,coren)

            case 'Se':
                if len(i.split(':')) <= 2:
                    try:
                        assert str(type(secretaria)) == '<class \'ClinicaSys.Classes.Secretaria\'>'
                    except Exception:
                        log_obj_n_existe('Secretaria',i.split(sep='=')[1].split(sep='->')[0])

                    match i.split('->')[1]:
                        case 'Medico':
                            secretaria.cadastrarFuncionarios(medico)
                        case 'Secretaria':
                            secretaria.cadastrarFuncionarios(secretaria)
                        case 'Enfermeira':
                            secretaria.cadastrarFuncionarios(enfermeira)
                            
                else:
                    nome = i.split(sep=':')[0][12:]
                    cpf = i.split(sep=':')[1]
                    data_nasc = i.split(sep=':')[2]
                    est_civil = i.split(sep=':')[3]
                    if(verifica_cpf(cpf,nome) and verifica_data(data_nasc,nome) and verifica_est_civil(est_civil,nome)):
                        secretaria=cls.Secretaria(nome,cpf,data_nasc,est_civil)
    print(comandos)
    print(pacientes[0])
    try:
        print(pacientes[1])
    except IndexError:
        pass
    print(secretaria)
    print(enfermeira)
    print(medico)


# P1=cls.Paciente('Augusto','91131839234','14/12/2003','Solteiro','Unimed',800)

# P2=cls.Paciente('Pedro','91131839234','14/12/2003','Casado','SUS',1000)

# M1 = cls.Medico('Augusto','91131839234','14/12/2003','Solteiro',123456)

# E1=cls.Enfermeira('Augusto','91131839234','14/12/2003','Solteiro',123456)

# S1=cls.Secretaria('Augusto','91131839234','14/12/2003','Solteiro')

# print(str(type(E1)))

