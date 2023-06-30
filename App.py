from ClinicaSys import Classes as cls
from ClinicaSys.Error import *

#abrindo arquivo txt e garantia de que haverá arquivo
while True:
    arqname=input('Digite o nome do arquivo que você deseja utilizar (sem sufixo de tipo, aceita-se apenas.txt): ')+'.txt'
    arq='Operacoes\\'+arqname

    try: 
        a = open(arq,'r')
    except FileNotFoundError:
        print(ArquivoNotFound(arqname))
    else:break


comandos = a.readlines()

#removendo o \n
for i in range(0,len(comandos)):
    comandos[i] = comandos[i][:-1]

pacientes=[]
medicos=[]
enfermeiras=[]


#criação dos objetos
for i in comandos:
    if i[0:2] == 'Pa':
        nome = i.split(sep=':')[0][11:]
        cpf = i.split(sep=':')[1]
        data_nasc = i.split(sep=':')[2]
        est_civil = i.split(sep=':')[3]
        plano = i.split(sep=':')[4]
        credito = i.split(sep=':')[5]
        if(verifica_cpf and verifica_convenio and verifica_data and verifica_est_civil and verifica_credito):
            pacientes.append(cls.Paciente(nome,cpf,data_nasc,est_civil,plano,credito))

print(pacientes)
#     if i[0:2] == 'Me':
#         pass
#     if i[0:2] == 'Se':
#         pass
#     if i[0:2] == 'Enf':
#         pass

# convenioTeste = cls.Convenio('Unimed',1200)
# P1=cls.Paciente('Augusto','91131839234','14/12/2003','Solteiro',convenioTeste)

# print(P1)

