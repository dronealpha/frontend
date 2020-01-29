#Autor:Diego Silva
#Data:28/01/2020
#Descrição:Compõe os arquivos json para disparo

from flask import request
from datetime import date

#classe para compor os json para o backend
class MontaJsonReq:

    #metodo monta json para notas de corte e religa
    def getNotas(self):
        if(request.form['acao']=='turnoon'):
            corte = 1
        else:
            corte = 0
        nova_nota = {
            'corte':corte
        }

        return nova_nota

    #metodo que retorna json com dados do cliente
    def getClientes(self):
        user = {
            'senha':request.form['password'],
            'nome':request.form['firstname'],
            'sobrenome':request.form['lastname'],
            'endereco':request.form['address'],
            'cpfcnpj':request.form['document'],
            'contato1':request.form['contact1'],
            'contato2':request.form['contact2']
        }

        return user

    #metodo que monta json do cadastro do dispositivo
    def getDispositivos(self):
        hoje = date.today() 
        novo_dev = {
            'data':'{}/{}/{}'.format(str(hoje.year),str(hoje.month),str(hoje.day)),
            'status':'1',
            'endereco':request.form['address']
            }

        return novo_dev

    #metodo rece code da request e verifica se deu sucesso ou falha
    def getSucesso(self, code):
        if(code==201):
            return '/cadastrostatus/sucesso'
        else:
            return '/cadastrostatus/falha'