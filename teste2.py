import mysql.connector



#Login
class login:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "trabalho_sa"
        )
        self.cursor = self.conn.cursor() 