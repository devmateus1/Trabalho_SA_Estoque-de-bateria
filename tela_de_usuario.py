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