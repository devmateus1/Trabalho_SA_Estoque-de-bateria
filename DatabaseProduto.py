import mysql.connector # Importa o modulo mysql.connector para conectar ao banco de dados MYSQL

class DataBase:
    def get_connection(self):
        # Conecta ao banco de dados MySQL com as credencias fornecidas
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "trabalho_sa"

        )
        self.cursor = self.conn.cursor() # Cria um cursor para exucutar comando SQL
        # Cria a tabela "Usuario" se ela não existir
        self.cursor.execute ('''CREATE TABLE IF NOT EXISTS produto(
                             idproduto int(11) NOT NULL,
                             tipo TEXT (255),
                             voltagem TEXT (255),
                             marca TEXT (255),
                             quantidade TEXT (255),
                             preco TEXT (255),
                             data TEXT (255)
                             );''')
        self.conn.commit() # Confirma a criação da tabela 
        print ("Conectado ao Banco de Dados") # Imprime uma mensagem de confirmação


    # Metódo para registrar um novo usuario no banco de dados
    def RegistrarNoBanco(self, tipo, voltagem, marca, quantidade, preco, data):
        self.cursor.execute("INSERT INTO produto (tipo, voltagem, marca, quantidade, preco, data) VALUES (%s ,%s ,%s ,%s, %s, %s)",(tipo, voltagem, marca, quantidade, preco, data)) # Insere os dados do usuario na tabela
        self.conn.commit() # Confirma a inseção dos dados

    # Metodo para buscar os dados de um usuario no banco de dados
    def ListarProduto(self, idproduto):
        self.cursor.execute("SELECT * FROM produto WHERE idproduto = %s", (idproduto)) 
        return self.cursor.fetchone() 