import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()#Criei o vinculo com a classe conexão
        self.db_connection = self.db_connection.conectar()#Conecto ao banco de dados
        self.con = self.db_connection.cursor()#Navega no meu banco
        
    def inserir(self, nome, telefone, endereco, dataDeNascimento):
        try:
            sql = "Insert into person(codigo, nome, telefone, endereco, dataDeNascimento) values('','{}','{}','{}','{}')".format(nome, telefone, endereco, dataDeNascimento)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Inserido!".format(self.con.rowcount)
        except Exception as erro:
            return erro