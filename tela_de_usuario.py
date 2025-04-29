'''from tkinter import *  # Importa todos os módulos do tkinter
from DataBase import Database
from tkinter import messagebox  # Importar o módulo de widgets temáticos do tkinter
from tkinter import ttk  # Importa o módulo de widgets temáticos do tkinter
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
        from Procura_Produto import AbrirProduto_cliente
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
    root.mainloop()  # Inicia o loop principal da janela'''


from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont

class TeldACASTRO:
    def __init__(self, root):
        self.root = root
        self.root.title("VGM Systems - Tela do Usuário")
        self.root.geometry("400x400")
        self.root.configure(background="#002333")
        self.root.resizable(False, False)
        self.center_window()

        # Fontes
        self.title_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        self.button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        self.label_font = tkFont.Font(family="Helvetica", size=12)

        # Frame principal
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(expand=True)

        # Header
        self.title_label = Label(self.main_frame, text="VGM Systems", font=self.title_font,
                                 bg="#002333", fg="white")
        self.title_label.pack(pady=(10, 5))

        self.subtitle_label = Label(self.main_frame, text="Painel do Usuário", font=self.label_font,
                                    bg="#002333", fg="#a0a0a0")
        self.subtitle_label.pack(pady=(0, 30))

        # Botões centralizados em coluna
        self.Produto = Button(self.main_frame, text="Consulta Produto", font=self.button_font,
                              bg="#0078D7", fg="white", activebackground="#0063B1",
                              activeforeground="white", borderwidth=0, width=25, pady=10,
                              command=self.produto)
        self.Produto.pack(pady=8)

        self.Fornecedor = Button(self.main_frame, text="Consulta Fornecedor", font=self.button_font,
                                 bg="#0078D7", fg="white", activebackground="#0063B1",
                                 activeforeground="white", borderwidth=0, width=25, pady=10,
                                 command=self.fornecedor)
        self.Fornecedor.pack(pady=8)

        self.Funcionario = Button(self.main_frame, text="Consulta Funcionário", font=self.button_font,
                                  bg="#0078D7", fg="white", activebackground="#0063B1",
                                  activeforeground="white", borderwidth=0, width=25, pady=10,
                                  command=self.funcionario)
        self.Funcionario.pack(pady=8)

        # Rodapé
        self.version_label = Label(self.main_frame, text="v1.0.0", font=("Helvetica", 8),
                                   bg="#002333", fg="#a0a0a0")
        self.version_label.pack(side=BOTTOM, pady=(30, 0))

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def produto(self):
        from Procura_Produto import AbrirProduto_cliente
        nova_janela = Toplevel(self.root)
        AbrirProduto_cliente(nova_janela)

    def fornecedor(self):
        from Procura_Fornecedor import Procura_Fornecedor
        nova_janela = Toplevel(self.root)
        Procura_Fornecedor(nova_janela)

    def funcionario(self):
        from tela_usuario_funcionario import TelaGeral
        nova_janela = Toplevel(self.root)
        TelaGeral(nova_janela)

if __name__ == "__main__":
    root = Tk()
    app = TeldACASTRO(root)
    root.mainloop()

