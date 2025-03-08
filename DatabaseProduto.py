import mysql.connector # Importa o modulo mysql.connector para conectar ao banco de dados MYSQL

class DataBase:
    def __init__(self):
        # Conecta ao banco de dados MySQL com as credencias fornecidas
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "trabalho_sa"

        )
        self.cursor = self.conn.cursor() # Cria um cursor para exucutar comando SQL
        # Cria a tabela "Usuario" se ela não existir
        self.cursor.execute ('''CREATE TABLE IF NOT EXISTS USUARIO(
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
        self.cursor.execute("INSERT INTO produto (tipo, voltagem, marca, quantidade, preco, data) VALUES (%s ,%s ,%s ,%s, %s, %s)",
                            (tipo, voltagem, marca, quantidade, preco, data)) # Insere os dados do usuario na tabela
        self.conn.commit() # Confirma a inseção dos dados

    # Metodo para alterar os dados de um usuario existente no banco de dados
    def alterar (self, tipo, voltagem, marca, quantidade, preco, data):
        self.conn.execute("UPDATE produto SET tipo=%s, voltagem=%s, ,marca=%s, quantidade=%s, preco=%s, data=%s",(tipo, voltagem, marca, quantidade, preco, data)) # Atualiza os dados do usuario com o id fornecido
        self.conn.commit() # Confirma a atualização dos dados

    # Metodo para excluir um usuario do banco de dados
    def excluir (self, tipo) :
        self.cursor.execute ("DELETE FROM produto WHERE tipo = %s", (tipo,)) # Excluir o usuario com idusuario
        self.conn.commit() # Confirma a exclusão dos dados

    # Metodo para buscar os dados de um usuario no banco de dados
    def buscar(self, tipo):
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM produto WHERE tipo= %s", (tipo,)) # Seleciona os dados do usuario com o id fornecido
        return self.cursor.fetchall() # Retorna os dados do usuario encontrado
    
    # Metodo chama quando a instancia da classe é destruida
    def __del__(self):
        self.conn.close() # Fecha a conexão com o banco de dados