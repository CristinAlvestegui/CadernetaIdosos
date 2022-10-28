import mysql.connector
from mysql.connector import errorcode

class conexao:
    def __init__(self):
        pass
    
    def conectar(self):
        try:
            self.db_connection = mysql.connector.connect(host="localhost",user="root",password="",database="bancoFlask")
            return self.db_connection
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR: 
                print('Banco de Dados não Existe!')
            elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Usuário ou senha inválido!')
            else:
                print(erro)
        else:
            self.db_connection.close()