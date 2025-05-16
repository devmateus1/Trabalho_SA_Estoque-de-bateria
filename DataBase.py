#pip install mysql-connector-python
import mysql.connector #Importa o modulo mysql.connector para conectar ao banco de dados MySQL
#pip install mysql-connector-python

def get_connection():
    return  mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'trabalho_sa'
)

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
    #DataBase Fornecedor
        self.conn.commit() #Confirma a criação da tabela


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------FORNECEDOR-------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def RegistrarNoBancoFornecedor(self,fornecedores,cpf,telefone,email,endereco,produto,quantidade):
        self.cursor.execute("INSERT INTO fornecedor(fornecedores, cpf, telefone, email, endereco, produto, quantidade) VALUES(%s, %s, %s, %s, %s, %s, %s)",(fornecedores, cpf, telefone, email, endereco, produto, quantidade)) #Insere os dados do usuario na tabela
        self.conn.commit() #Confirma a inserção dos dados
        self.conn.close()

    def alterarFornecedor(self,idfornecedor,fornecedores,cpf,telefone,email,endereco,produto,quantidade):
        self.cursor.execute("UPDATE fornecedor SET fornecedores=%s, cpf=%s, telefone=%s, email=%s, endereco=%s, produto=%s,quantidade=%s WHERE idfornecedor=%s",
                            (fornecedores,cpf,telefone,email,endereco,produto,quantidade,idfornecedor)) #Atualiza os dados do usuario com id oferecido
        self.conn.commit() #Confirma a atualização do dados 
        self.conn.close()

    def buscar_fornecedor(self, idfornecedor):
        query = "SELECT * FROM fornecedor WHERE idfornecedor = %s"
        self.cursor.execute(query, (idfornecedor,))
        return self.cursor.fetchone() 

    def removerFornecedor(self,idfornecedor):
        self.cursor.execute("DELETE FROM fornecedor WHERE idfornecedor=%s", (idfornecedor,))
        self.conn.commit()

    def buscar_nome_fornecedor(self):
        self.cursor.execute("SELECT fornecedores, idfornecedor FROM fornecedor")
        resultados = self.cursor.fetchall()
        return [(nome, idf) for nome, idf in resultados if nome is not None]








#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------FUNCIONARIOS-----------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def RegistrarNoBancofuncionario(self, cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco):
        # Insere um novo funcionário no banco de dados
        self.cursor.execute("INSERT INTO funcionario(cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                            (cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco))
        self.conn.commit()  # Confirma a inserção dos dados

    def removerfuncionario(self,idfuncionario):
        self.cursor.execute("DELETE FROM funcionario WHERE idfuncionario=%s",(idfuncionario,))
        self.conn.commit()

    def alterarfuncionario(self, idfuncionario, cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco):
        self.cursor.execute("UPDATE funcionario SET cpf=%s, nome=%s, telefone=%s, email=%s, dataDeContratacao=%s, cargo=%s,salario=%s, endereco=%s WHERE idfuncionario=%s",
                            (cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco, idfuncionario)) #Atualiza os dados do usuario com id oferecido
        self.conn.commit() #Confirma a atualização do dados 
        self.conn.close()


    def buscar_funcionario(self, id_funcionario):
        query = "SELECT * FROM funcionario WHERE idfuncionario = %s"
        self.cursor.execute(query, (id_funcionario,))

    def buscar_funcionario(self, id_funcionario):
         query = "SELECT * FROM funcionario WHERE id = %s"
         query = "SELECT * FROM funcionario WHERE idfuncionario = %s"
         self.cursor.execute(query, (id_funcionario,))
         return self.cursor.fetchone() 

    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------PRODUTO----------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


        # Metódo para registrar um novo usuario no banco de dados
    def RegistrarNoBanco_Produto(self, tipo, voltagem, marca, quantidade, preco, data, cod_fornecedor):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produto (tipo, voltagem, marca, quantidade, preco, data, idfornecedor) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                       (tipo, voltagem, marca, quantidade, preco, data, cod_fornecedor))  # Inserir dados
        conn.commit()  # Confirmar a inserção
        conn.close()
        cursor.close()

    # Metodo para buscar os dados de um usuario no banco de dados
    def buscar_produto(self, id_produto):
        query = """
        SELECT produto.*, fornecedor.*
        FROM produto
        INNER JOIN fornecedor ON fornecedor.idfornecedor = produto.idfornecedor
        WHERE produto.idproduto = %s
        """
        self.cursor.execute(query, (id_produto,))
        return self.cursor.fetchone()
    
    def removerproduto(self, idproduto):
        try:
            # Verifica se o produto existe usando o nome correto da coluna
            self.cursor.execute("SELECT COUNT(*) FROM produto WHERE idproduto=%s", (idproduto,))
            resultado = self.cursor.fetchone()

            if resultado[0] == 0:
                print(f"Produto com id {idproduto} não encontrado.")
                return

            # Deleta o produto, usando o nome correto da coluna
            self.cursor.execute("DELETE FROM produto WHERE idproduto=%s", (idproduto,))
            self.conn.commit()

            print(f"Produto com id {idproduto} e suas compras relacionadas foram removidos com sucesso.")
        
        except Exception as e:
            self.conn.rollback()  # Desfaz a transação em caso de erro
            print(f"Ocorreu um erro: {e}")

    def alterarproduto(self, idproduto, tipo, voltagem, marca, quantidade, preco, data,cod_fornecedor):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE produto SET tipo=%s, voltagem=%s, marca=%s, quantidade=%s, preco=%s, data=%s, idfornecedor=%s WHERE idproduto=%s", 
                       (tipo, voltagem, marca, quantidade, preco, data, cod_fornecedor,idproduto))  # Inserir dados
        conn.commit()  # Confirmar a inserção
        conn.close()
        cursor.close()
        
    #Fazer login
    def FazerLogin(self, usuario, senha):
        self.cursor.execute("""SELECT * FROM usuario WHERE usuario = %s AND senha = %s""", (usuario, senha))
        self.conn.commit() # Confirma a inseção dos dados
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------CLIENTE----------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def RegistrarNoBancoCliente(self,nomecliente,cpf,telefone,endereco):
        self.cursor.execute("INSERT INTO cliente (nome, cpf, telefone, endereco) VALUES (%s ,%s, %s, %s)",(nomecliente, cpf, telefone, endereco)) # Insere os dados do usuario na tabela
        self.conn.commit() # Confirma a inseção dos dados
        

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------LOGIN------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

     
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

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------Busca produto e usuário---------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def buscar_produtos_por_cliente(self, id_cliente):
    query = """
        SELECT p.idproduto, p.nome, p.tipo, p.preco
        FROM cliente cl
        INNER JOIN compra c ON cl.idcliente = c.idcliente
        INNER JOIN item i ON c.idCompra = i.idcompra
        INNER JOIN produto p ON i.idproduto = p.idproduto
        WHERE cl.idcliente = %s
    """
    self.cursor.execute(query, (id_cliente,))
    return self.cursor.fetchall()  # Retorna todos os produtos comprados pelo cliente

