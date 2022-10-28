from flask import Flask, render_template, request
from model import model
import this

this.rg = ""
this.cpf = ""
this.sus = ""
this.nome = ""
this.nomeDaMae= ""
this.apelido= ""
this.sexo = ""
this.uf = ""
this.nacionalidade = ""
this.pais = ""
this.ler = ""
this.escolaridade = ""
this.raca = ""
this.etnia = ""
this.religiao = ""
this.profissao = ""
this.telefone = ""
this.endereco = ""
this.data = ""
this.dados = ""
this.modelo = model()
this.codigo = 0
this.msg = ""
this.campo = ""
this.dado = ""

pessoa = Flask(__name__)

@pessoa.route('/')
def index():
    return render_template('index.html', titulo="Página Principal")

@pessoa.route('/home')
def menu():
    return render_template('home.html', titulo="Home")


if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)