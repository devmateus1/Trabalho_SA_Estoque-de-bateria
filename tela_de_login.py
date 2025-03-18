from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database

# Criação da tela
jan = Tk()
jan.title("SL Systems - Painel de Acesso")
jan.geometry("500x500")
jan.configure(background="#002333")
jan.resizable(width=False, height=False)

# Criando forma do usuário fazer login (Usuário e Senha)
LoginLabel = Label(text="Usuário: ", font=("Century Gothic", 20), bg="#002333", fg="white")
LoginLabel.place(x=45, y=80)
LoginEntry = ttk.Entry(width=30)
LoginEntry.place(x=155, y=94)

SenhaLabel = Label(text="Senha: ", font=("Century Gothic", 20), bg="#002333", fg="white")
SenhaLabel.place(x=57, y=125)
SenhaEntry = ttk.Entry(width=30, show="•")
SenhaEntry.place(x=155, y=140)

# Função para fazer login
def FazerLogin():
    usuario = LoginEntry.get()
    senha = SenhaEntry.get()

    # try:
    #     # Verificando login do usuário 'ADM'
    #     if usuario == 'ADM' and senha == '1234':
    #         from tela_de_adm import TelaLoginCadastro
    #         TelaLoginCadastro(jan)  # Passando a janela principal como parâmetro para a nova tela
    #     else:
            # Conexão com o banco de dados para validar o login do usuário
    db = Database()
    db.cursor.execute("""SELECT * FROM usuario WHERE usuario = %s AND senha = %s""", (usuario, senha))
    VerifyLogin = db.cursor.fetchone()

            # Se o login for validado no banco de dados
    if VerifyLogin:
        messagebox.showinfo(title="INFO LOGIN", message="Acesso Confirmado, Bem-vindo!")
        adm = VerifyLogin[0]

        if adm == 1:
            from tela_de_adm import TelaLoginCadastro
            root_menu = Tk()  
            TelaLoginCadastro(root_menu)
            root_menu.mainloop()

        else:
        

            from tela_de_usuario import TeldACASTRO
            root_menu = Tk() 
            TeldACASTRO(root_menu)
            root_menu.mainloop()
    else:
                # Se não encontrar o usuário no banco de dados
        messagebox.showinfo(title="INFO LOGIN", message="Acesso Negado. Verifique se está cadastrado no sistema!")
   
    messagebox.showerror(title="Erro", message=f"Ocorreu um erro: {str(e)}")

# Botão de login
LoginButton = ttk.Button(text="LOGIN", width=15, command=FazerLogin)
LoginButton.place(x=130, y=335)

# Registrar um novo usuário (essa parte não foi implementada, mas pode ser adicionada conforme necessário)

if __name__ == "__main__":
    jan.mainloop()
