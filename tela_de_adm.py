


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database

class TelaLoginCadastro:

    def __init__(self, root):
        self.root = root
        self.root.title("Tela de adm - Painel de Acesso")
        self.root.geometry("600x300")
        self.root.configure(background="#002333")
       

        # Botões de navegação
        self.ProdutosButton = ttk.Button(self.root, text = "Produtos", width = 10, command = self.TelaProdutos)
        self.ProdutosButton.place(x=100, y=30)

        self.FuncionariosButton = ttk.Button(self.root, text = "Funcionarios", width = 15, command = self.TelaFuncionarios)
        self.FuncionariosButton.place(x=200, y=30)

        self.FornecedoresButton = ttk.Button(self.root, text = "Fornecedores", width = 15, command = self.TelaFornecedores)
        self.FornecedoresButton.place(x=350, y=30)

        

        self.BV = Label(self.root, text = "BEM VINDO", font = ("Times New Roman", 20))
        self.BV.place(x = 675, y = 30)

    def TelaProdutos(self):
        from Produto import AbrirProduto
        AbrirProduto(self.root)
        self.ProdutosButton.place(x=5000)

    def TelaFuncionarios(self):
        from Cadastro_de_funcionarios2 import Abrir_funcionario
        Abrir_funcionario(self.root)
        self.ProdutosButton.place(x=5000)

    def TelaFornecedores(self):
        from Cadastro_Fornecedor import Abrir_Fornecedor
        Abrir_Fornecedor(self.root)
        self.ProdutosButton.place(x=5000)

   

if __name__ == "__main__":
    jan = Tk()
    tela = TelaLoginCadastro(jan)
    jan.mainloop()
