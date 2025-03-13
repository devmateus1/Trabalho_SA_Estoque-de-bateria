
# #Login
# class login:
#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host = "localhost",
#             user = "root",
#             password = "",
#             database = "trabalho_sa"
      
import mysql.connector
     
class login:
    def __init__(self):
        # Conectar ao banco de dados (exemplo com psycopg2, adapte conforme necessário)
        self.connection =mysql.connector.connect(
            host="localhost",
            database="trabalho_sa",
            user="root",
            password=""
        )
        self.cursor = self.connection.cursor()  # Criação do cursor
    
    def __del__(self):
        # Fechar a conexão com o banco de dados ao destruir o objeto
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
