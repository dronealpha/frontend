
#Autor:Diego Silva
#Data:27/01/2020
#Descrição:Classe mãe de requisições
class ReqServidor:

    #cosntrutor para inicializar atributos privados
    def __init__ (self, servidorip, porta, rota):
        self.__servidorip = servidorip
        self.__porta = porta
        self.__rota = rota

    #retornar ip servidor
    def getServidorIp(self):
        return self.__servidorip

    #retornar porta de comunicacão
    def getPorta(self):
        return self.__porta

    #retorna rota de acesso
    def getRota(self):
        return self.__rota