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
this.descricao = ""
this.dose = ""
this.dataMed = ""
this.medico = ""
this.dados = ""
this.modelo = model()
this.codigo = 0
this.msg = ""
this.campo = ""
this.dado = ""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo="Página Principal")

@app.route('/alergias.html', methods=['GET','POST'])
def alergias():
    return render_template('alergias.html', titulo="Alergias")

@app.route('/ambiental.html', methods=['GET','POST'])
def ambiental():
    return render_template('ambiental.html', titulo="Ambiental")

@app.route('/antropometricos.html', methods=['GET','POST'])
def antropometricos():
    return render_template('antropometricos.html', titulo="Antropometrico")

@app.route('/medicamentos.html', methods=['GET','POST'])
def medicamentos():
    if request.method == 'POST':
        this.descricao = request.form['tNovoDescricao']
        this.dose = request.form['tNovoDose']
        this.dataMed = request.form['tNovoDataMed']
        this.medico = request.form['tNovoMedico']
        this.dados = this.modelo.inserirMed(this.descricao, this.dose, this.dataMed, this.medico)
    return render_template('medicamentos.html', titulo="Medicação", resultado=this.dados)

@app.route('/cadastroCuidador.html', methods=['GET','POST'])
def cadastroCuidador():
    return render_template('cadastroCuidador.html', titulo="Cadastro Cuidador")

@app.route('/cadastroVES.html', methods=['GET','POST'])
def cadastroVES():
    return render_template('cadastroVES.html', titulo="Cadastro VES")

@app.route('/cadIdoso.html', methods=['GET','POST'])
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

@app.route('/cadSaude.html', methods=['GET','POST'])
def cadSaude():
    return render_template('cadSaude.html', titulo="Cadastro Saude")

@app.route('/cirurgia.html', methods=['GET','POST'])
def cirurgias():
    return render_template('cirurgia.html', titulo="Cirurgias")

@app.route('/cntrlDeQuedas.html', methods=['GET','POST'])
def ctrlDeQuedas():
    return render_template('cntrlDeQuedas.html', titulo="Quedas")

@app.route('/cntrlGlicemia.html', methods=['GET','POST'])
def cntrlGlicemia():
    return render_template('cntrlGlicemia.html', titulo="Glicemia")

@app.route('/cntrlPressaoArterial.html', methods=['GET','POST'])
def cntrlPressaoArterial():
    return render_template('cntrlPressaoArterial.html', titulo="Pressão Arterial")

@app.route('/complementar.html', methods=['GET','POST'])
def complementar():
    return render_template('complementar.html', titulo="Complementar")

@app.route('/controlePeso.html', methods=['GET','POST'])
def controlePeso():
    return render_template('controlePeso.html', titulo="Peso")

@app.route('/dorCronica.html', methods=['GET','POST'])
def dorCronica():
    return render_template('dorCronica.html', titulo="Dores Cronicas")

@app.route('/habitosVida.html', methods=['GET','POST'])
def habitosVida():
    return render_template('habitosVida.html', titulo="Habitos de Vida")

@app.route('/home.html', methods=['GET','POST'])
def menu():
    return render_template('home.html', titulo="Home")

@app.route('/pessoaRef.html', methods=['GET','POST'])
def pessoaRef():
    return render_template('pessoaRef.html', titulo="Pessoas de Referencia")

@app.route('/saudeBucal.html', methods=['GET','POST'])
def saudeBucal():
    return render_template('saudeBucal.html', titulo="Saude Bucal")

@app.route('/vacinacao.html', methods=['GET','POST'])
def vacinacao():
    return render_template('vacinacao.html', titulo="Vacinas")

if __name__ == '__main__':
    app.run(debug=True, port=5000)