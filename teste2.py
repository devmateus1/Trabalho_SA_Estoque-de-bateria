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


        #class TeldACASTRO:
    #jan = Tk()
    # jan.title("Tela de adm - Painel de Acesso")
    # jan.geometry("600x300")
    # jan.configure(background="#002333")
    # jan.resizable(width=False, height=False)



    # Produto = Button (text="PRODUTO", width=10)
    # Produto.place (x=100 ,y=30)

    # Fornecedor = Button (text="FORNECEDOR", width=15)
    # Fornecedor.place (x=200 ,y= 30)

    # Funcionario = Button (text="FUNCIONARIO", width=15)
    # Funcionario .place (x=350 ,y=30)
   
    # jan.mainloop()