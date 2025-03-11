import mysql.connector # Importa o modulo mysql.connector para conectar ao banco de dados MYSQL

class db_produto:
    def get_connection(self):
        # Conecta ao banco de dados MySQL com as credencias fornecidas
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "trabalho_sa"

        )
        self.cursor = self.conn.cursor() # Cria um cursor para exucutar comando SQL


    # Metódo para registrar um novo usuario no banco de dados
    def RegistrarNoBanco_Produto(self, tipo, voltagem, marca, quantidade, preco, data):
        self.cursor.execute("INSERT INTO produto (tipo, voltagem, marca, quantidade, preco, data) VALUES (%s ,%s ,%s ,%s, %s, %s)",(tipo, voltagem, marca, quantidade, preco, data)) # Insere os dados do usuario na tabela
        self.conn.commit() # Confirma a inseção dos dados

    # Metodo para buscar os dados de um usuario no banco de dados
    def Listar_Produto(self, idproduto):
        self.cursor.execute("SELECT * FROM produto WHERE idproduto = %s", (idproduto)) 
        return self.cursor.fetchone() 