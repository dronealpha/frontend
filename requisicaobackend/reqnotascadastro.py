#Autor:Diego Silva
#Data:28/01/2020
#Descrição: script para montar dados de cadastro de notas de corte e religa
from sys import path
path.append('/requisicaobackend')
from requisicaobackend.servidorrequisicoes import ReqServidor

class NotascadastroReq(ReqServidor):

    def __init__(self, servidorip, porta, rota, jsonenvio):
        super(NotascadastroReq, self).__init__(servidorip, porta, rota)
        self.__jsonenvio = jsonenvio

    def getUrlCallback(self):
        return 'http://{}:{}{}'.format(str(self.getServidorIp()),str(self.getPorta()),self.getRota())

    def getJsonDados(self):
        return self.__jsonenvio