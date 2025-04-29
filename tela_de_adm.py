



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

'''from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#from DataBase import Database

class TelaLoginCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Administrativo")
        self.root.geometry("500x500")
        self.root.configure(background="#002333")
        self.root.resizable(width=False, height=False)

        # Boas-vindas
        self.label_title = Label(self.root, text="BEM-VINDO, ADM!", font=("Helvetica", 18, "bold"), fg="white", bg="#002333")
        self.label_title.pack(pady=20)

        # Frame central para botões
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(pady=10)

        # Lista de botões (texto, comando)
        botoes = [
            ("Cadastrar Fornecedor", self.TelaFornecedores),
            ("Consultar Fornecedor", self.TelaConsulta),
            ("Cadastrar Produto", self.TelaProduto),
            ("Consultar Produto", self.Telaconsultaproduto),
            ("Cadastrar Funcionário", self.TelaFuncionario),
            ("Consultar Funcionário", self.TelaconsultaFuncionario),
        ]

        for texto, comando in botoes:
            btn = ttk.Button(self.main_frame, text=texto, width=30, command=comando)
            btn.pack(pady=5)

    # Funções de navegação
    def TelaFornecedores(self):
        from Cadastro_Fornecedor import Abrir_Fornecedor
<<<<<<< HEAD
        nova_janela = Toplevel(self.root)
        Abrir_Fornecedor(nova_janela)
       
    

    def TelaConsulta(self):
        from Produto_cadastrar import AbrirProduto_cadastro
        nova_janela = Toplevel()  # Sem self.root
        nova_janela.geometry("+1920+100")  # Posição inicial na segunda tela
        AbrirProduto_cadastro(nova_janela)

=======
        Abrir_Fornecedor(self.root)

    def TelaConsulta(self):
        from Procura_Delete_Alterar_Fornecedor import Procura_DeleteEAlterarFornecedor
        Procura_DeleteEAlterarFornecedor(self.root)
>>>>>>> 9d4d5e8edc52856258f73f09e95a015bb5b1bd56

    def TelaProduto(self):
        from Produto_cadastrar import AbrirProduto_cadastro
        AbrirProduto_cadastro(self.root)

    def Telaconsultaproduto(self):
        from Produto_adm import AbrirProduto_adm
        AbrirProduto_adm(self.root)

    def TelaFuncionario(self):
        from Cadastro_de_funcionarios2 import Abrir_funcionario
        Abrir_funcionario(self.root)

    def TelaconsultaFuncionario(self):
        from TelaGeralFuncionarios import TelaGeral
        TelaGeral(self.root)

# Execução
if __name__ == "__main__":
    root = Tk()
    app = TelaLoginCadastro(root)
    root.mainloop()'''

from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

class TelaAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("VGM Systems - Painel de Administração")
        self.root.geometry("500x500")
        self.root.configure(background="#002333")
        self.root.resizable(False, False)

        # Fontes
        self.title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        self.section_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.button_font = tkFont.Font(family="Helvetica", size=10)

        # --- SCROLLING SETUP ---
        container = Frame(self.root, bg="#002333")
        container.pack(fill=BOTH, expand=True)

        canvas = Canvas(container, bg="#002333", highlightthickness=0)
        scrollbar = Scrollbar(container, orient=VERTICAL, command=canvas.yview)
        self.scrollable_frame = Frame(canvas, bg="#002333")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Título
        Label(self.scrollable_frame, text="BEM-VINDO ADMINISTRADOR",
              font=self.title_font, bg="#002333", fg="white").pack(pady=(10, 30))

        # Botões
        self.create_section("FORNECEDORES", [
            ("Cadastrar Fornecedor", self.TelaFornecedores),
            ("Consultar Fornecedores", self.TelaConsulta)
        ])

        self.create_section("PRODUTOS", [
            ("Cadastrar Produto", self.TelaProduto),
            ("Consultar Produtos", self.Telaconsultaproduto)
        ])

        self.create_section("FUNCIONÁRIOS", [
            ("Cadastrar Funcionário", self.TelaFuncionario),
            ("Consultar Funcionários", self.TelaconsultaFuncionario)
        ])

        # Rodapé
        Label(self.scrollable_frame, text="Sistema de Administração v1.0",
              font=("Arial", 8), bg="#002333", fg="white").pack(pady=10)

    def create_section(self, title, buttons):
        Label(self.scrollable_frame, text=title, font=self.section_font,
              bg="#002333", fg="white").pack(anchor=W, padx=30, pady=(10, 5))
        for text, command in buttons:
            Button(self.scrollable_frame, text=text, command=command,
                   font=self.button_font, bg="#0078D7", fg="white",
                   activebackground="#005fa3", activeforeground="white",
                   relief="flat", padx=10, pady=8).pack(fill=X, padx=30, pady=5)

    # Métodos das telas
    def TelaFornecedores(self):
        from Cadastro_Fornecedor import Abrir_Fornecedor
        Abrir_Fornecedor(self.root)

    def TelaConsulta(self):
        from Procura_Delete_Alterar_Fornecedor import Procura_DeleteEAlterarFornecedor
        Procura_DeleteEAlterarFornecedor(self.root)

    def TelaProduto(self):
        from Produto_cadastrar import AbrirProduto_cadastro
        AbrirProduto_cadastro(self.root)

    def Telaconsultaproduto(self):
        from Produto_adm import AbrirProduto_adm
        AbrirProduto_adm(self.root)

    def TelaFuncionario(self):
        from Cadastro_de_funcionarios2 import Abrir_funcionario
        Abrir_funcionario(self.root)

    def TelaconsultaFuncionario(self):
        from TelaGeralFuncionarios import TelaGeral
        TelaGeral(self.root)

if __name__ == "__main__":
    root = Tk()
    app = TelaAdmin(root)
    root.mainloop()
