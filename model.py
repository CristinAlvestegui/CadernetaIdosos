import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()#Criei o vinculo com a classe conexão
        self.db_connection = self.db_connection.conectar()#Conecto ao banco de dados
        self.con = self.db_connection.cursor()#Navega no meu banco
        
    def inserir(self, nome, apelido, sus, rg, cpf, nomeDaMae, dataDeNascimento, sexo, uf, nacionalidade, pais, ler, escolaridade, raca, etnia, religiao):
        try:
            sql = "Insert into person(nome, apelido, sus, rg, cpf, nomeDaMae, dataDeNascimento, sexo, uf, nacionalidade, pais, ler, escolaridade, raca, etnia, religiao) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(nome, apelido, sus, rg, cpf, nomeDaMae, dataDeNascimento, sexo, uf, nacionalidade, pais, ler, escolaridade, raca, etnia, religiao)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Inserido!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def inserirMed(self, descricao, dose, dataMed, medico):
        try:
            sql = "Insert into medicine(codigo, descricao, dose, dataMed, medico) values('','{}','{}','{}','{}')".format(descricao, dose, dataMed, medico)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Inserido!".format(self.con.rowcount)
        except Exception as erro:
            return erro