from tkinter import *
from tkinter import ttk, messagebox
import tkinter.font as tkFont
from DataBase import Database

class ProcuraFornecedor:
    def __init__(self, root):
        """Inicializa a aplicação e configura a interface"""
        self.root = root
        self.root.title("VGM Systems - Consulta Fornecedor")
        self.root.configure(bg="#002333")
        self.root.resizable(False, False)
        self.center_window(800, 500)

        # Instancia o banco de dados
        self.db = Database()

        # Cria fontes
        self.create_fonts()

        # Cria widgets da interface
        self.create_layout()

    def create_fonts(self):
        """Define as fontes utilizadas na interface"""
        self.title_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        self.label_font = tkFont.Font(family="Helvetica", size=12)
        self.button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

    def create_layout(self):
        """Cria a estrutura da interface, incluindo labels, entradas e botões"""
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(expand=True, fill=BOTH)

        # Título da tela
        Label(self.main_frame, text="FORNECEDORES | USUÁRIO", font=self.title_font, bg="#002333", fg="white").pack(pady=(10, 20))

        # Frame de campos de entrada
        self.form_frame = Frame(self.main_frame, bg="#002333")
        self.form_frame.pack()

        # Criação dos campos de entrada
        self.entries = []
        self.create_form_fields()

        # Criação dos botões
        self.create_buttons()

    def create_form_fields(self):
        """Cria os campos de entrada para consulta do fornecedor"""
        campos = [
            "ID do Fornecedor",
            "Nome do Fornecedor",
            "CPF do Fornecedor",
            "Telefone do Fornecedor",
            "Email do Fornecedor",
            "Endereço do Fornecedor",
            "Produto Fornecido",
            "Quantia de Produto"
        ]

        # Adiciona os campos de entrada
        for i, campo in enumerate(campos):
            self.add_label_entry(self.form_frame, campo, i)

    def add_label_entry(self, parent, text, row):
        """Adiciona um label e entry ao layout"""
        Label(parent, text=text + ":", font=self.label_font, bg="#002333", fg="white").grid(
            row=row, column=0, sticky=W, padx=10, pady=5
        )
        entry = ttk.Entry(parent, width=40)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.entries.append(entry)

    def create_buttons(self):
        """Cria os botões de interação"""
        btn_frame = Frame(self.main_frame, bg="#002333")
        btn_frame.pack(pady=20)

        # Botões para buscar, limpar e voltar
        ttk.Button(btn_frame, text="BUSCAR", width=20, command=self.buscar_fornecedor).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="LIMPAR", width=20, command=self.limpar_campos).grid(row=0, column=1, padx=10)
        Button(
            btn_frame, text="VOLTAR AO MENU", font=self.button_font, bg="#0078D7", fg="white", 
            activebackground="#0063B1", activeforeground="white", borderwidth=0, width=20, pady=5, 
            command=self.voltar_menu
        ).grid(row=0, column=2, padx=10)

    def buscar_fornecedor(self):
        """Realiza a busca de fornecedor por ID"""
        id_fornecedor = self.entries[0].get()
        if not id_fornecedor:
            messagebox.showerror("Erro", "Preencha o campo de ID")
            return

        fornecedor = self.db.buscar_fornecedor(id_fornecedor)
        if fornecedor:
            self.preencher_campos(fornecedor)
        else:
            messagebox.showerror("Erro", "Fornecedor não encontrado")
            self.limpar_campos()

    def preencher_campos(self, fornecedor):
        """Preenche os campos com as informações do fornecedor encontrado"""
        for i in range(1, 8):
            self.entries[i].delete(0, END)
            self.entries[i].insert(0, fornecedor[i])

    def limpar_campos(self):
        """Limpa todos os campos de entrada"""
        for entry in self.entries:
            entry.delete(0, END)

    def voltar_menu(self):
        """Fecha a tela atual e retorna ao menu do usuário"""
        self.root.destroy()
        from tela_usuario import TeldACASTRO
        nova_root = Tk()
        TeldACASTRO(nova_root)
        nova_root.mainloop()

    def center_window(self, width, height):
        """Centraliza a janela na tela"""
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')


if __name__ == "__main__":
    root = Tk()
    app = ProcuraFornecedor(root)
    root.mainloop()
