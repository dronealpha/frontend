#Autor:Diego Silva
#Data:27/01/2020
#Descrição:Script para criação de rotas de cadastro
#biblioteca flask e flask_restful para tabalhar com micro serviços
from sys import path
path.append('/requisicaobackend')
from flask import Flask , render_template, request, redirect, url_for
from requisicaobackend.servidorrequisicoes import ReqServidor
from requisicaobackend.reqclientecadastro import ClienteCadastroReq
from requisicaobackend.reqdispositivocadastro import DispositivocadastroReq
from requisicaobackend.reqnotascadastro import NotascadastroReq
from requisicaobackend.montajsonreq import MontaJsonReq
from requisicaobackend.postdados import PostDados


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cadastrocliente')
def addCliente():
    return render_template('cadastrocliente.html')

#rotas para direcionamento de cadastro cliente, dispositivo e nota
@app.route('/efetuacadastrocliente', methods=['POST'])
def efetuacadastroclinte():
    login = request.form['username']
    login = '/cliente/{}'.format(login)
    clt = MontaJsonReq()

    dados = ClienteCadastroReq('127.0.0.1','5001',login,clt.getClientes())
    pst = PostDados(dados)
        
    return redirect(clt.getSucesso(pst.getDisparapost().status_code))


@app.route('/efetuacadastrodispositivo', methods=['POST'])
def efetuacadastrodispositivo():
    device = request.form['macid']
    device = '/cadastrodispositivo/{}'.format(device)
    dvc = MontaJsonReq()
   
    dados = DispositivocadastroReq('127.0.0.1','5001',device,dvc.getDispositivos())
    pst = PostDados(dados)

    return redirect(dvc.getSucesso(pst.getDisparapost().status_code))

@app.route('/efetuacadastronotas', methods=['POST'])
def efetuacadastronotas():
    nota = request.form['macid']
    nota = '/cadastronota/{}'.format(nota)
    nt = MontaJsonReq()

    dados = NotascadastroReq('127.0.0.1','5001',nota,nt.getNotas())
    pst = PostDados(dados)

    return redirect(nt.getSucesso(pst.getDisparapost().status_code))

#validação do sucesso ou falha no cadastro
@app.route('/cadastrostatus/<string:statuscad>')
def cadastrostatus(statuscad):
    print(statuscad)
    return render_template('resultado.html', codigo = statuscad)

@app.route('/cadastrodispositivo')
def addDispositivo():
    return render_template('cadastrodispositivo.html')

@app.route('/notas')
def addNotas():
    return render_template('cadastronotas.html') 
app.run(port=5005, debug=True)
