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

@pessoa.route('/', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.nome     = request.form['tNovoNome']
        this.telefone = request.form['tNovoTelefone']
        this.endereco = request.form['tNovoEndereco']
        this.data     = request.form['tNovaData']
        this.dados    = this.modelo.inserir(this.nome, this.telefone, this.endereco, this.data)
    return render_template('index.html', titulo="Página Principal", resultado=this.dados)

@pessoa.route('/consultar.html', methods=['GET','POST'])
def consultarTudo():
    if request.method == 'POST':
        this.codigo   = request.form['tNovoCodigo']
        this.msg = this.modelo.consultar(this.codigo)
    return render_template('home.html', titulo="Consultar", dados=this.msg)


if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)