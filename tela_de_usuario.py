from tkinter import * #Importa todos os mudulos do tkinter
from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
from tkinter import ttk

 #from DataBase import DataBase

#Criar a janela
class TeldACASTRO:
    jan = Tk()
    jan.title("Tela de usuario - Painel de Acesso")
    jan.geometry("600x300")
    jan.configure(background="#002333")
    jan.resizable(width=False, height=False)

    text1 = Label (text="Tela Usuario", width=49)
    text1.place (x=100 ,y=20)

    Produto = Button (text="PRODUTO", width=10)
    Produto.place (x=100 ,y=50)

    Fornecedor = Button (text="FORNECEDOR", width=15)
    Fornecedor.place (x=200 ,y= 50)


    Funcionario = Button (text="FUNCIONARIO", width=15) 
    Funcionario .place (x=335 ,y=50)
   
    jan.mainloop()