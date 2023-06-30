class Erro(Exception):
    def __init__(self, causa):
        self.__causa = causa

    @property
    def _causa(self):
        return self.__causa



class ArquivoNotFound(Erro):
    def __init__(self,causa):
        super().__init__(causa)
        self.__nome_invalido=self._causa

    def __str__(self):
        return f'Não foi possível encontrar dentro dos aqruivos operáveis, o arquivo {self.__nome_invalido}'
    


class erroCPF(Erro):
    def __init__(self,causa):
        super().__init__(causa)
        self.__valor_inserido=self._causa

    def __str__(self):
        return f'para um CPF ser válido, o mesmo necessita conter um total de 11 caracteres, sendo esses apenas dígitos, o valor inserido \"{self.__valor_inserido}\"'
    


class ConvenioInvalido(Erro):
    def __init__(self,causa):
        super().__init__(causa)
        self.__ConvenioInvalido = causa
    
    def __str__(self):
        return f'O Convênio {self.__ConvenioInvalido} não é válido, trabalhamos apenas com Unimed, SUS e IPE'
    


class est_civil_invalido(Erro):
    def __init__(self,causa):
        super().__init__(causa)
        self.__estadoInvalido = causa
    
    def __str__(self):
        return f'O Estado Cívil {self.__estadoInvalido} não é válido aceitamos apenas Solteiro, Casado ou Viúva(o)'
    


class data_Invalida(Erro):
    def __init__(self,causa):
        super().__init__(causa)
        self.__data = causa
    
    def __str__(self):
        return f'A data informada {self.__estadoInvalido} não é válida, exemplo do formato aceito \"31/12/2023\".'
    


class creditos_Invalidos(Erro):
    def __init__(self,causa):
        super().__init__(causa)
        self.__quantia = causa
    
    def __str__(self):
        return f'A quantia informada {self.__estadoInvalido} não é um número'
    
    

def verifica_cpf(cpf,nome):
        log=open('Saídas\\Log.txt','a')        
        try:
            assert len(cpf) == 11
        except AssertionError:
            log.writelines(f'\nFoi detectado um erro ao tentar criar {nome}, por isso o objeto não foi criado. Erro: {erroCPF(cpf)} não possui 11 dígitos')
            return False
        else:
            try:
                int(cpf)
            except ValueError:
                log.writelines(f'\nFoi detectado um erro ao tentar criar {nome}, por isso o objeto não foi criado. Erro: {erroCPF(cpf)} não possui apenas dígitos')
                return False
            else:
                return True



def verifica_est_civil(est_civil,nome):
    log=open('Saídas\\Log.txt','a')   
    try:
            assert est_civil.upper() == 'SOLTEIRO' or est_civil.upper() == 'CASADO' or est_civil.upper() == 'VIÚVO' or est_civil.upper() == 'VIÚVA'
    except AssertionError:
        log.writelines(f'\nFoi detectado um erro ao tentar criar {nome}, por isso o objeto não foi criado. Erro: {est_civil_invalido(est_civil)}')



def verifica_convenio(convenio,nome):
    log=open('Saídas\\Log.txt','a')   
    try:
            assert convenio.upper() == 'UNIMED' or convenio.upper() == 'SUS' or convenio.upper() == 'IPE'
    except AssertionError:
        log.writelines(f'\nFoi detectado um erro ao tentar criar {nome}, por isso o objeto não foi criado. Erro: {ConvenioInvalido(convenio)}')



def verifica_data(data,nome):
    log=open('Saídas\\Log.txt','a')   
    try:
            assert data[2] == '/' and data[5] == '/' and len(data) == 10
    except AssertionError:
        log.writelines(f'\nFoi detectado um erro ao tentar criar {nome}, por isso o objeto não foi criado. Erro:{data_Invalida}')
    else:
        try:
            dia=int(data[0:1])
            mes=int(data[3:4])
            ano=int(data[6:9])
        except ValueError:
            log.writelines(f'\nFoi detectado um erro ao tentar criar {nome}, por isso o objeto não foi criado. Erro:{data_Invalida}')
        else:
            try:
                assert (dia < 28 and mes == 2) or (dia < 30 and mes in [4,6,9,11]) or (dia <31 and mes in [1,3,5,7,8,10,12]) and ano > 1900
            except AssertionError:
                log.writelines(f'\nFoi detectado um erro ao tentar criar {nome}, por isso o objeto não foi criado. Verifique se a sua data de nascimento existe, ex: não existe dia 30/02 nem 31/04')



def verifica_credito(credito,nome):
    log=open('Saídas\\Log.txt','a')   
    try:
        int(credito)
    except:
        log.writelines(f'\nFoi detectado um erro ao tentar criar {nome}, por isso o objeto não foi criado. Erro: {creditos_Invalidos(credito)}')
        return False
    else: return True