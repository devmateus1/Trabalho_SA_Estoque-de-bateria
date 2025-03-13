
# from tkinter import * #Importa todos os mudulos do tkinter
# from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
# from tkinter import ttk
# #from DataBase import DataBase

# # Criar a janela
# jan = Tk()
# jan.title("SL Systens - Painel de Acesso")
# jan.geometry("600x300")
# jan.configure(background="#002333")
# jan.resizable(width=False, height=False)

# loginlabel = Label (text="LOGIN", bg="#002333" , fg="white")
# loginlabel.place (x=200 , y=70)
# loginEntry = ttk.Entry (width=15)
# loginEntry.place (x=250 ,y=70)



# Senhalabel = Label (text="SENHA", bg="#002333" , fg="white")
# Senhalabel.place (x=200 , y=100)
# SenhaEntry = ttk.Entry (width=15)
# SenhaEntry.place (x=250 ,y=100)


# Login = Button (text="LOGIN", width=10)
# Login.place (x=200 ,y=140)

# jan.mainloop()




# from tkinter import *
# from tkinter import messagebox
# from tkinter import ttk
# from teste2 import login

# class TelaLoginCadastro:

#     def __init__(self, root):
#         self.root = root
#         self.root.title("Menu")
#         self.root.geometry("500x500")
#         self.root.configure(background="#f6f3ec")
#         self.root.resizable(width=False, height=False)

#         # Botões de navegação
     

#         self.FornecedoresButton = ttk.Button(self.root, text = "Fornecedores", width = 40, command = self.TelaFornecedores)
#         self.FornecedoresButton.place(x=800, y=435)

       

#         self.BV = Label(self.root, text = "BEM VINDO", font = ("Times New Roman", 20))
#         self.BV.place(x = 675, y = 30)



    

#     def TelaFornecedores(self):
#         from Cadastro_Fornecedor import Abrir_Fornecedor
#         Abrir_Fornecedor(self.root)
#         self.ProdutosButton.place(x=5000)



# root = Tk()
# tela = TelaLoginCadastro(root)
# root.mainloop()