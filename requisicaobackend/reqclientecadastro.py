#Autor:Diego Silva
#Data:27/01/2020
#Descrição:Script para post no cadastro de clientes

#importando path do script de origem
from sys import path
path.append('/requisicaobackend')
from requisicaobackend.servidorrequisicoes import ReqServidor


class ClienteCadastroReq(ReqServidor):

    def __init__(self, servidorip, porta, rota, jsonenvio):
        super(ClienteCadastroReq, self).__init__(servidorip, porta, rota)
        self.__jsonenvio = jsonenvio

    #metodo monta url de callback
    def getUrlCallback(self):
        return 'http://{}:{}{}'.format(str(self.getServidorIp()),str(self.getPorta()),self.getRota())

    #retorna json para fazer post
    def getJsonDados(self):
        return self.__jsonenvio



