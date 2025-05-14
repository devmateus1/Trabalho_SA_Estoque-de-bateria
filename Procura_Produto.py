from tkinter import *
from tkinter import ttk, messagebox
from DataBase import Database
import tkinter.font as tkFont

class AbrirProduto_cliente:
    def __init__(self, root):
        self.root = root
        self.root.configure(background="#002333")

        # Fontes
        self.title_font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        self.label_font = tkFont.Font(family="Helvetica", size=10)
        self.button_font = tkFont.Font(family="Helvetica", size=10, weight="bold")

        # Frame principal
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

        # Cabeçalho
        self.title_label = Label(self.main_frame, text="BUSCA DE PRODUTO | CLIENTE:",
                                 font=self.title_font, bg="#002333", fg="white")
        self.title_label.pack(pady=(10, 20))

        # Frame dos campos
        form_frame = Frame(self.main_frame, bg="#002333")
        form_frame.pack()

        # Entradas e labels
        self.entries = {}
        campos = [
            ("ID DO PRODUTO", 1, 1),
<<<<<<< Updated upstream
            ("ID DO FORNECEDOR", 1, 0),
            ("TIPO DA BATERIA", 2, 0),
            ("VOLTAGEM DA BATERIA", 3, 0),
            ("MARCA DA BATERIA", 4, 0),
            ("QUANTIDADE DA BATERIA", 5, 0),
            ("PREÇO DA BATERIA", 6, 0),
            ("DATA DE VALIDADE", 7, 0)
=======
            ("TIPO DA BATERIA", 1, 0),
            ("VOLTAGEM DA BATERIA", 2, 0),
            ("MARCA DA BATERIA", 3, 0),
            ("QUANTIDADE DA BATERIA", 4, 0),
            ("PREÇO DA BATERIA", 5, 0),
            ("DATA DE VALIDADE", 6, 0)
>>>>>>> Stashed changes
        ]

        for texto, linha, coluna in campos:
            label = Label(form_frame, text=texto + ":", font=self.label_font, bg="#002333", fg="white")
            label.grid(row=linha, column=coluna * 2, sticky=E, pady=5, padx=5)
            entry = ttk.Entry(form_frame, width=30)
            entry.grid(row=linha, column=coluna * 2 + 1, pady=5, padx=5)
            self.entries[texto] = entry

        # Botões
        botoes_frame = Frame(self.main_frame, bg="#002333")
        botoes_frame.pack(pady=20)

        Button(botoes_frame, text="BUSCAR", font=self.button_font, bg="#0078D7", fg="white",
               activebackground="#0063B1", activeforeground="white", borderwidth=0,
               width=18, pady=8, command=self.buscarproduto).pack(side=LEFT, padx=10)

        Button(botoes_frame, text="LIMPAR CAMPOS", font=self.button_font, bg="#0078D7", fg="white",
               activebackground="#0063B1", activeforeground="white", borderwidth=0,
               width=18, pady=8, command=self.LimparCampos).pack(side=LEFT, padx=10)

        Button(botoes_frame, text="VOLTAR AO MENU", font=self.button_font, bg="#0078D7", fg="white",
               activebackground="#0063B1", activeforeground="white", borderwidth=0,
               width=18, pady=8, command=self.juntar_funcoes).pack(side=LEFT, padx=10)

        # Rodapé
        self.version_label = Label(self.main_frame, text="v1.0.0", font=("Helvetica", 8),
                                   bg="#002333", fg="#a0a0a0")
        self.version_label.pack(side=BOTTOM, pady=(10, 0))

    def LimparCampos(self):
        for entry in self.entries.values():
            entry.delete(0, END)

    def buscarproduto(self):
        idproduto = self.entries["ID DO PRODUTO"].get()
        if not idproduto:
            messagebox.showerror(title="Erro", message="PREENCHA O CAMPO DE ID")
            return

        db = Database()
        usuario = db.buscar_produto(idproduto)
        if usuario:
            chaves = list(self.entries.keys())
            for i in range(len(chaves)):  # pula o ID
                self.entries[chaves[i]].delete(0, END)
                self.entries[chaves[i]].insert(0, usuario[i])
                
        else:
            messagebox.showerror("Erro", "Produto não encontrado")
            self.LimparCampos()

    def voltar_menu(self):
        self.root.destroy()
        from tela_usuario import TeldACASTRO
        root = Tk()
        TeldACASTRO(root)
        root.mainloop()

    def limpar_tela(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def juntar_funcoes(self):
        self.limpar_tela()
        self.voltar_menu()


if __name__ == "__main__":
    root = Tk()
    root.title("USUÁRIO - PRODUTO - CLIENTE")
    root.geometry("800x500")
    root.configure(background="#002333")
    root.resizable(False, False)

    app = AbrirProduto_cliente(root)
    root.mainloop()
