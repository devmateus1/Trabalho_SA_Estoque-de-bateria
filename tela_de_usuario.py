from tkinter import *  # Importa todos os módulos do tkinter
from tkinter import messagebox  # Importar o módulo de widgets temáticos do tkinter
from tkinter import ttk  # Importa o módulo de widgets temáticos do tkinter
from DataBase import Database
# Criar a janela
class TeldACASTRO:
    def __init__(self, root):
        self.root = root  # Atribui a janela recebida à instância da classe

        # Configurações da janela
        self.root.title("Tela de usuario - Painel de Acesso")
        self.root.geometry("600x300")
        self.root.configure(background="#002333")
        self.root.resizable(width=False, height=False)

        # Configurações do Label
        self.text1 = Label(self.root, text="Tela Usuario", width=49)
        self.text1.place(x=100, y=20)
        

        # Botões de navegação
        self.Produto = ttk.Button(self.root, text="Consulta Produto", width=30, command=self.produto)
        self.Produto.place(x=5, y=50)

        self.Fornecedor = ttk.Button(self.root, text="Consulta Fornecedor", width=30, command=self.fornecedor)
        self.Fornecedor.place(x=200, y=50)

        self.Funcionario = ttk.Button(self.root, text="Consulta Funcionario", width=30, command=self.funcionario)
        self.Funcionario.place(x=400, y=50)
#TESTE
    def produto(self):
        from Produto_cliente import AbrirProduto_cliente
        AbrirProduto_cliente(self.root)  # Chama a função corretamente
        self.ProdutosButton.place(x=5000)

    def fornecedor(self):
        from Procura_Fornecedor import Procura_Fornecedor
        Procura_Fornecedor(self.root)  # Chama a função corretamente
        self.ProdutosButton.place(x=5000)

    def funcionario(self):
        from tela_usuario_funcionario import TelaGeral
        TelaGeral(self.root)  # Chama a função corretamente
        self.ProdutosButton.place(x=5000)

# Cria a janela principal e passa ela para a classe
if __name__ == "__main__":
    root = Tk()  # Instancia a janela principal
    app = TeldACASTRO(root)  # Passa a janela para a classe TeldACASTRO
    root.mainloop()  # Inicia o loop principal da janela
