import mysql.connector #Importa o modulo mysql.connector para conectar ao banco de dados MySQL
class Database:
    def __init__(self):
        #Conecta ao banco de dados MySQL com as credenciais forncedas
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'trabalho_sa'
        )
        self.cursor = self.conn.cursor() #Cria um cursor para executar comandos MySQL
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `fornecedor` (
                        `idfornecedor` int(11) NOT NULL,
                        `fornecedores` text DEFAULT NULL,
                        `cpf` text DEFAULT NULL,
                        `telefone` text DEFAULT NULL,
                        `email` text DEFAULT NULL,
                        `endereco` text DEFAULT NULL,
                        `produto` text DEFAULT NULL, 
                        `quantidade` int(11) DEFAULT NULL

        );''')

        self.conn.commit() #Confirma a criação da tabela
    def RegistrarNoBanco(self,fornecedores,cpf,telefone,email,endereco,produto,quantidade):
        self.cursor.execute("INSERT INTO fornecedor(fornecedores, cpf, telefone, email, endereco, produto, quantidade) VALUES(%s, %s, %s, %s, %s, %s, %s)",(fornecedores, cpf, telefone, email, endereco, produto, quantidade)) #Insere os dados do usuario na tabela
        self.conn.commit() #Confirma a inserção dos dados

                        
    def buscar(self,idfornecedor):
        self.cursor.execute("SELECT * FROM fornecedor WHERE idfornecedor=%s",(idfornecedor,)) #Seleciona os dados do usuario com o id fornecido
        return self.cursor.fetchone() #Retorna oos dados do usuario encontrado
    

        # Metódo para registrar um novo usuario no banco de dados
    def RegistrarNoBanco_Produto(self, tipo, voltagem, marca, quantidade, preco, data):
        self.cursor.execute("INSERT INTO produto (tipo, voltagem, marca, quantidade, preco, data) VALUES (%s ,%s ,%s ,%s, %s, %s)",(tipo, voltagem, marca, quantidade, preco, data)) # Insere os dados do usuario na tabela
        self.conn.commit() # Confirma a inseção dos dados

    # Metodo para buscar os dados de um usuario no banco de dados
    def Listar_Produto(self, idproduto):
        self.cursor.execute("SELECT * FROM produto WHERE idproduto = %s", (idproduto)) 
        return self.cursor.fetchone() 