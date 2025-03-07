from tkinter import * #Importa todos os mudulos do tkinter
from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
from tkinter import ttk
from tela_de_adm import*
#from DataBase import DataBase

# Criar a janela
jan = Tk()
jan.title("SL Systens - Painel de Acesso")
jan.geometry("600x300")
jan.configure(background="#002333")
jan.resizable(width=False, height=False)

loginlabel = Label (text="LOGIN", bg="#002333" , fg="white")
loginlabel.place (x=200 , y=70)
loginEntry = ttk.Entry (width=15)
loginEntry.place (x=250 ,y=70)


Senhalabel = Label (text="SENHA", bg="#002333" , fg="white")
Senhalabel.place (x=200 , y=100)
SenhaEntry = ttk.Entry (width=15)
SenhaEntry.place (x=250 ,y=100)


Login = Button (text="LOGIN", width=10)
Login.place (x=250 ,y=140)


seleciona = "SELECT nomes FROM usuario WHERE nomes ='{}'".format(loginEntry)
""" #cursor.execute(seleciona)
resultado = cursor.fetchall()
if len(resultado)!=0: #Verifica se o retorno contém alguma linha
        print('Usuario Já Cadastrado')
else:
        print('Cadastro realizado')
        """
        
jan.mainloop()

