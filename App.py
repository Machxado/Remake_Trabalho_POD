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
                    match i.split(sep='=')[1].split(sep='->')[0]:
                        case 'internar':
                            npaciente=int(i.split(sep='->')[1][-1])-1
                            medico.internar(pacientes[npaciente])
                        case 'liberar':
                            npaciente= int(i.split(sep='->')[1][-1])-1
                            medico.liberar(pacientes[npaciente])
                        case 'diagnosticar':
                            npaciente= int(i.split(sep='->')[1].split(sep=':')[0][-1])-1
                            medico.diagnosticar(pacientes[npaciente],i.split(sep=':')[1])
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
                    match i.split(sep='=')[1].split(sep='->')[0]:
                        case 'cadastrar':
                            npaciente=int(i.split(sep='->')[1][-1])-1
                            enfermeira.cadastrarPaciente(pacientes[npaciente])
                        case 'relatorio':
                            npaciente=int(i.split(sep='->')[1][-1])-1
                            enfermeira.gerarRelatorio(medico,pacientes[npaciente])
                
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
    print(pacientes[1])
    print(secretaria)
    print(enfermeira)
    print(medico)


# P1=cls.Paciente('Augusto','91131839234','14/12/2003','Solteiro','Unimed',800)

# P2=cls.Paciente('Pedro','91131839234','14/12/2003','Casado','SUS',1000)

# M1 = cls.Medico('Augusto','91131839234','14/12/2003','Solteiro',123456)

# E1=cls.Enfermeira('Augusto','91131839234','14/12/2003','Solteiro',123456)

# S1=cls.Secretaria('Augusto','91131839234','14/12/2003','Solteiro')

# print(str(type(E1)))

