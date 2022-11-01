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

@pessoa.route('/alergias.html')
def alergias():
    return render_template('alergias.html', titulo="Alergias")

@pessoa.route('/ambiental.html')
def ambiental():
    return render_template('ambiental.html', titulo="Ambiental")

@pessoa.route('/antropometricos.html')
def antropometricos():
    return render_template('antropometricos.html', titulo="Antropometrico")

@pessoa.route('/avalIdoso.html')
def avalIdoso():
    return render_template('avalIdoso.html', titulo="Avaliação do Idoso")

@pessoa.route('/cadastroCuidador.html')
def cadastroCuidador():
    return render_template('cadastroCuidador.html', titulo="Cadastro Cuidador")

@pessoa.route('/cadastroVES.html')
def cadastroVES():
    return render_template('cadastroVES.html', titulo="Cadastro VES")

@pessoa.route('/cadIdoso.html')
def cadIdoso():
    return render_template('cadIdoso.html', titulo="Cadastro do Idoso")

@pessoa.route('/cadSaude.html')
def cadSaude():
    return render_template('cadSaude.html', titulo="Cadastro Saude")

@pessoa.route('/cirurgia.html')
def cirurgias():
    return render_template('cirurgia.html', titulo="Cirurgias")

@pessoa.route('/cntrlDeQuedas.html')
def ctrlDeQuedas():
    return render_template('cntrlDeQuedas.html', titulo="Quedas")

@pessoa.route('/cntrlGlicemia.html')
def cntrlGlicemia():
    return render_template('cntrlGlicemia.html', titulo="Glicemia")

@pessoa.route('/cntrlPressaoArterial.html')
def cntrlPressaoArterial():
    return render_template('cntrlPressaoArterial.html', titulo="Pressão Arterial")

@pessoa.route('/complementar.html')
def complementar():
    return render_template('complementar.html', titulo="Complementar")

@pessoa.route('/controlePeso.html')
def controlePeso():
    return render_template('controlePeso.html', titulo="Peso")

@pessoa.route('/dorCronica.html')
def dorCronica():
    return render_template('dorCronica.html', titulo="Dores Cronicas")

@pessoa.route('/habitosVida.html')
def habitosVida():
    return render_template('habitosVida.html', titulo="Habitos de Vida")

@pessoa.route('/home.html')
def menu():
    return render_template('home.html', titulo="Home")

@pessoa.route('/pessoaRef.html')
def pessoaRef():
    return render_template('pessoaRef.html', titulo="Pessoas de Referencia")

@pessoa.route('/saudeBucal.html')
def saudeBucal():
    return render_template('saudeBucal.html', titulo="Saude Bucal")

@pessoa.route('/vacinacao.html')
def vacinacao():
    return render_template('vacinacao.html', titulo="Vacinas")

if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)