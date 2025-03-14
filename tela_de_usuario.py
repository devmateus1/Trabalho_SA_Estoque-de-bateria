from tkinter import * #Importa todos os mudulos do tkinter
from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
from tkinter import ttk

import DataBase

#  Criar a janela
class TeldACASTRO:
     def __init__(self, root):
        self.root = root
        self.root.title("Menu de usuario")
        self.root.geometry("500x500")
        self.root.configure(background="#002333")
        self.root.resizable(width=False, height=False)

         # Botões de navegação
     

        self.FornecedoresButton = ttk.Button(self.root, text = "Fornecedores", width = 30, command = self.TelaFornecedores)
        self.FornecedoresButton.place(x=100, y=70)

        

        



    

        self.BV = Label(self.root, text = "BEM VINDO USUARIO!!", font = ("Times New Roman", 15))
        self.BV.place(x = 50, y = 15)



    

        def TelaFornecedores(self):
            from Cadastro_Fornecedor import Abrir_Fornecedor
            Abrir_Fornecedor(self.root)
            self.ProdutosButton.place(x=5000)
        
   


   
root = Tk()
tela = TeldACASTRO(root)
root.mainloop()
