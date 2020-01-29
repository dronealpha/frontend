#Autor:Diego Silva
#Data:27/01/2020
#Descrição:
import requests as rq
import json
from requisicaobackend.reqclientecadastro import ClienteCadastroReq

HEADERS = {'content-type':'application/json'}


class PostDados:
    def __init__(self, dadospost):
        self.__dadospost = dadospost

    def getDisparapost(self):
        return rq.post(url=self.__dadospost.getUrlCallback(), data=json.dumps(self.__dadospost.getJsonDados()), headers=HEADERS)
