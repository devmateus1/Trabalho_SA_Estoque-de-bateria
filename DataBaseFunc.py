import mysql.connector

class Database:
    def __init__(self):
        # Conecta ao banco de dados MySQL com as credenciais fornecidas
        self.conn = mysql.connector.connect(
            host='localhost',  # Endereço do servidor MySQL
            user='root',  # Nome do usuário do banco de dados
            password='',  # Senha do usuário (deve ser configurada corretamente)
            database='trabalho_sa'  # Nome do banco de dados
        )
        
        self.cursor = self.conn.cursor()  # Cria um cursor para executar comandos SQL
        
        # Cria a tabela 'funcionario' caso ela não exista no banco de dados
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `funcionario` (
                        `idfuncionario` int(11) NOT NULL,
                        `cpf` text DEFAULT NULL,
                        `nome` text DEFAULT NULL,
                        `telefone` text DEFAULT NULL,
                        `email` text DEFAULT NULL,
                        `dataDeContratacao` text DEFAULT NULL,
                        `cargo` text DEFAULT NULL,
                        `salario` text DEFAULT NULL,
                        `endereco` int(11) DEFAULT NULL
        );''')
        
        self.conn.commit()  # Confirma a criação da tabela no banco de dados

    def RegistrarNoBanco(self, cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco):
        # Insere um novo funcionário no banco de dados
        self.cursor.execute("INSERT INTO funcionario(cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                            (cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco))
        self.conn.commit()  # Confirma a inserção dos dados

    def buscar(self, idfuncionario):
        # Seleciona os dados do funcionário com o ID fornecido
        self.cursor.execute("SELECT * FROM funcionario WHERE idfuncionario=%s", (idfuncionario,))
        return self.cursor.fetchone()  # Retorna os dados do funcionário encontrado
