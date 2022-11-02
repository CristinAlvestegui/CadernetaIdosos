from flask import Flask, render_template, request
from model import model
import this

this.rg = ""
this.cpf = ""
this.sus = ""
this.nome = ""
this.nomeDaMae= ""
this.data = ""
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
this.rg = ""
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

@pessoa.route('/alergias.html', methods=['GET','POST'])
def alergias():
    return render_template('alergias.html', titulo="Alergias")

@pessoa.route('/ambiental.html', methods=['GET','POST'])
def ambiental():
    return render_template('ambiental.html', titulo="Ambiental")

@pessoa.route('/antropometricos.html', methods=['GET','POST'])
def antropometricos():
    return render_template('antropometricos.html', titulo="Antropometrico")

@pessoa.route('/avalIdoso.html', methods=['GET','POST'])
def avalIdoso():
    return render_template('avalIdoso.html', titulo="Avaliação do Idoso")

@pessoa.route('/cadastroCuidador.html', methods=['GET','POST'])
def cadastroCuidador():
    return render_template('cadastroCuidador.html', titulo="Cadastro Cuidador")

@pessoa.route('/cadastroVES.html', methods=['GET','POST'])
def cadastroVES():
    return render_template('cadastroVES.html', titulo="Cadastro VES")

@pessoa.route('/cadIdoso.html', methods=['GET','POST'])
def cadIdoso():
    if request.method == 'POST':
        this.nome     = request.form['tNovoNome']
        this.apelido = request.form['tNovoApelido']
        this.sus = request.form['tNovoSus']
        this.rg     = request.form['tNovoRg']
        this.cpf = request.form['tNovoCpf']
        this.nomeDaMae = request.form['tNovoNomeDaMae']
        this.data = request.form['tNovoData']
        this.sexo = request.form['tNovoSexo']
        this.uf = request.form['tNovoUf']
        this.nacionalidade = request.form['tNovoNacionalidade']
        this.pais = request.form['tNovoPais']
        this.ler = request.form['tNovoLer']
        this.escolaridade = request.form['tNovoEscolaridade']
        this.raca = request.form['tNovoRaca']
        this.etnia = request.form['tNovoEtnia']
        this.religiao = request.form['tNovoReligiao']
        this.dados    = this.modelo.inserir(this.nome, this.apelido, this.sus, this.rg, this.cpf, this.nomeDaMae, this.data, this.sexo, this.uf, this.nacionalidade, this.pais, this.ler, this.escolaridade, this.raca, this.etnia, this.religiao)
    return render_template('cadIdoso.html', titulo="Cadastro do Idoso", resultado=this.dados)

@pessoa.route('/cadSaude.html', methods=['GET','POST'])
def cadSaude():
    return render_template('cadSaude.html', titulo="Cadastro Saude")

@pessoa.route('/cirurgia.html', methods=['GET','POST'])
def cirurgias():
    return render_template('cirurgia.html', titulo="Cirurgias")

@pessoa.route('/cntrlDeQuedas.html', methods=['GET','POST'])
def ctrlDeQuedas():
    return render_template('cntrlDeQuedas.html', titulo="Quedas")

@pessoa.route('/cntrlGlicemia.html', methods=['GET','POST'])
def cntrlGlicemia():
    return render_template('cntrlGlicemia.html', titulo="Glicemia")

@pessoa.route('/cntrlPressaoArterial.html', methods=['GET','POST'])
def cntrlPressaoArterial():
    return render_template('cntrlPressaoArterial.html', titulo="Pressão Arterial")

@pessoa.route('/complementar.html', methods=['GET','POST'])
def complementar():
    return render_template('complementar.html', titulo="Complementar")

@pessoa.route('/controlePeso.html', methods=['GET','POST'])
def controlePeso():
    return render_template('controlePeso.html', titulo="Peso")

@pessoa.route('/dorCronica.html', methods=['GET','POST'])
def dorCronica():
    return render_template('dorCronica.html', titulo="Dores Cronicas")

@pessoa.route('/habitosVida.html', methods=['GET','POST'])
def habitosVida():
    return render_template('habitosVida.html', titulo="Habitos de Vida")

@pessoa.route('/home.html', methods=['GET','POST'])
def menu():
    return render_template('home.html', titulo="Home")

@pessoa.route('/pessoaRef.html', methods=['GET','POST'])
def pessoaRef():
    return render_template('pessoaRef.html', titulo="Pessoas de Referencia")

@pessoa.route('/saudeBucal.html', methods=['GET','POST'])
def saudeBucal():
    return render_template('saudeBucal.html', titulo="Saude Bucal")

@pessoa.route('/vacinacao.html', methods=['GET','POST'])
def vacinacao():
    return render_template('vacinacao.html', titulo="Vacinas")

if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)