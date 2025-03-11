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
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `funcionario` (
                        `idfun` int(11) NOT NULL,
                        `id_func` text DEFAULT NULL,
                        `nome` text DEFAULT NULL,
                        `telefone` text DEFAULT NULL,
                        `email` text DEFAULT NULL,
                        `cargo` text DEFAULT NULL,
                        `salario` text DEFAULT NULL,
                        `cidade` text DEFAULT NULL,
                        `bairro` text(11) DEFAULT NULL

        );''')
        self.conn.commit() #Confirma a criação da tabela
    def RegistrarNoBanco(self,id_func,nome,telefone,email, cargo,salario, cidade,bairro):
        self.cursor.execute("INSERT INTO funcionario(id_func,nome,telefone,email, cargo,salario, cidade,bairro) VALUES(%s, %s, %s, %s, %s, %s, %s,%s)",(id_func, nome, telefone, email, cargo, salario, cidade,bairro)) #Insere os dados do usuario na tabela
        self.conn.commit() #Confirma a inserção dos dados
    
    def buscar(self,idfun):
        self.cursor.execute("SELECT * FROM funcionario WHERE idfun=%s",(idfun,)) #Seleciona os dados do usuario com o id fornecido
        return self.cursor.fetchone() #Retorna oos dados do usuario encontrado