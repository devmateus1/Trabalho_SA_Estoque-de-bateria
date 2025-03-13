



# from tkinter import *
# from tkinter import messagebox
# from tkinter import ttk
# from teste2 import login

# class TelaLoginCadastro:

#     def __init__(self, root):
#         self.root = root
#         self.root.title("Tela de adm - Painel de Acesso")
#         self.root.geometry("600x300")
#         self.root.configure(background="#002333")
       

#         # Botões de navegação
#         self.ProdutosButton = ttk.Button(self.root, text = "Produtos", width = 10, command = self.TelaProdutos)
#         self.ProdutosButton.place(x=100, y=30)

#         self.FuncionariosButton = ttk.Button(self.root, text = "Funcionarios", width = 15, command = self.TelaFuncionarios)
#         self.FuncionariosButton.place(x=200, y=30)

#         self.FornecedoresButton = ttk.Button(self.root, text = "Fornecedores", width = 15, command = self.TelaFornecedores)
#         self.FornecedoresButton.place(x=350, y=30)

        

#         self.BV = Label(self.root, text = "BEM VINDO", font = ("Times New Roman", 20))
#         self.BV.place(x = 675, y = 30)

#     def TelaProdutos(self):
#         from Produto import AbrirProduto
#         AbrirProduto(self.root)
#         self.ProdutosButton.place(x=5000)

#     def TelaFuncionarios(self):
#         from Cadastro_de_funcionarios2 import Abrir_funcionario
#         Abrir_funcionario(self.root)
#         self.ProdutosButton.place(x=5000)

#     def TelaFornecedores(self):
#         from Cadastro_Fornecedor import Abrir_Fornecedor
#         Abrir_Fornecedor(self.root)
#         self.ProdutosButton.place(x=5000)

   

# if __name__ == "__main__":
#     jan = Tk()
#     tela = TelaLoginCadastro(jan)
#     jan.mainloop()


# Criar a janela

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database

class TelaLoginCadastro:

    def __init__(self, root):
        self.root = root
        self.root.title("Menu de adm")
        self.root.geometry("500x500")
        self.root.configure(background="#002333")
        self.root.resizable(width=False, height=False)

        # Botões de navegação
     

        self.FornecedoresButton = ttk.Button(self.root, text = "Fornecedores", width = 30, command = self.TelaFornecedores)
        self.FornecedoresButton.place(x=100, y=100)

        self.FornecedoresButton = ttk.Button(self.root, text = "Consulta Fornecedores", width = 30, command = self.TelaConsulta)
        self.FornecedoresButton.place(x=100, y=140)


        self.FornecedoresButton = ttk.Button(self.root, text = "Funcionario", width = 30, command = self.TelaFuncionario)
        self.FornecedoresButton.place(x=100, y=200)

        self.BV = Label(self.root, text = "BEM VINDO", font = ("Times New Roman", 15))
        self.BV.place(x = 100, y = 30)



    

    def TelaFornecedores(self):
        from Cadastro_Fornecedor import Abrir_Fornecedor
        Abrir_Fornecedor(self.root)
        self.ProdutosButton.place(x=5000)
        
    def TelaConsulta(self):
        from Procura_Delete_Alterar_Fornecedor import Procura_DeleteEAlterarFornecedor
        Procura_DeleteEAlterarFornecedor(self.root)
        self.ProdutosButton.place(x=5000)



    def TelaFuncionario(self):
        from Cadastro_de_funcionarios2 import Abrir_funcionario
        Abrir_funcionario(self.root)
        self.ProdutosButton.place(x=5000)

root = Tk()
tela = TelaLoginCadastro(root)
root.mainloop()

