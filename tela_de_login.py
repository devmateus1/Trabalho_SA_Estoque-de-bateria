from tkinter import * 
from tkinter import messagebox 
from tkinter import ttk 

from teste2 import login

#Criação da tela
jan = Tk() 
jan.title("SL Systens - Painel de Acesso") 
jan.geometry("500x500") 
jan.configure(background = "#002333") 
jan.resizable(width = False, height = False) 



#Criando forma do usuario fazer login (Usuario e Senha)
LoginLabel = Label(text = "Usuario: ", font = ("Century Gothic", 20), bg = "#002333", fg = "white") 
LoginLabel.place(x = 45, y = 80) 
LoginEntry = ttk.Entry(width = 30)  
LoginEntry.place(x = 155, y = 94)

SenhaLabel = Label(text = "Senha: ", font = ("Century Gothic", 20 ), bg = "#002333", fg = "white") 
SenhaLabel.place(x = 57, y = 125)
SenhaEntry = ttk.Entry(width = 30, show = "•") 
SenhaEntry.place(x = 155, y = 140)

#Fazer login
def FazerLogin():

    usuario = LoginEntry.get()
    senha = SenhaEntry.get()

    db = login() 
    db.cursor.execute("""SELECT * FROM usuario WHERE usuario = %s AND senha = %s""", (usuario, senha))
    VerifyLogin = db.cursor.fetchone()

    if VerifyLogin:
        messagebox.showinfo(title = "INFO LOGIN", message = "Acesso Confirmado, Bem Vindo!")

        from tela_de_adm import  TeldACASTRO
        TeldACASTRO()
        
    else:
        messagebox.showinfo(title = "INFO LOGIN", message = "Acesso Negado. Verifique se esta cadastrado no sistema!")

LoginButton = ttk.Button(text = "LOGIN", width = 15, command = FazerLogin)
LoginButton.place(x = 130, y = 335)

#Registrar um novo usuario


 
jan.mainloop()