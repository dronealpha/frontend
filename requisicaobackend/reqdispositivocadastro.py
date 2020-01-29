#Autor:Diego Silva
#Data:28/01/2020
#Descrição:Script para post de do cadastro de dispositivos

#importando path do script de origem
from sys import path
path.append('/requisicaobackend')
from requisicaobackend.servidorrequisicoes import ReqServidor

class DispositivocadastroReq(ReqServidor):

    def __init__(self, servidorip, porta, rota, jsonenvio):
        super(DispositivocadastroReq, self).__init__(servidorip, porta, rota)
        self.__jsonenvio = jsonenvio

    def getUrlCallback(self):
        return 'http://{}:{}{}'.format(str(self.getServidorIp()),str(self.getPorta()),self.getRota())

    def getJsonDados(self):
        return self.__jsonenvio