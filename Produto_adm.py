from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database
import customtkinter as ctk


class AbrirProduto_adm:
    def __init__(self, root):
        self.root = root
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(expand=True, fill=BOTH)

        Cadastrotitulo = Label(self.main_frame, text="CADASTRO DE PRODUTO | ADM :", bg="#002333", fg="white")
        Cadastrotitulo.place(x=230, y=10)

        # Labels e Entradas
        Label(self.main_frame, text="TIPO DA BATERIA :", bg="#002333", fg="white").place(x=55, y=50)
        self.TipoProdutoEntry = ttk.Entry(self.main_frame, width=30)
        self.TipoProdutoEntry.place(x=170, y=50)

        Label(self.main_frame, text="VOLTAGEM DA BATERIA :", bg="#002333", fg="white").place(x=20, y=90)
        self.VoltagemEntry = ttk.Entry(self.main_frame, width=30)
        self.VoltagemEntry.place(x=170, y=90)

        Label(self.main_frame, text="MARCA DA BATERIA :", bg="#002333", fg="white").place(x=40, y=130)
        self.MarcaEntry = ttk.Entry(self.main_frame, width=30)
        self.MarcaEntry.place(x=170, y=130)

        Label(self.main_frame, text="QUANTIDADE DA BATERIA :", bg="#002333", fg="white").place(x=8, y=170)
        self.QuantidadeEntry = ttk.Entry(self.main_frame, width=30)
        self.QuantidadeEntry.place(x=170, y=170)

        Label(self.main_frame, text="PREÇO DA BATERIA :", bg="#002333", fg="white").place(x=45, y=210)
        self.PrecoEntry = ttk.Entry(self.main_frame, width=30)
        self.PrecoEntry.place(x=170, y=210)

        Label(self.main_frame, text="DATA DE VALIDADE :", bg="#002333", fg="white").place(x=45, y=250)
        self.DataProdutoEntry = ttk.Entry(self.main_frame, width=30)
        self.DataProdutoEntry.place(x=170, y=250)

        Label(self.main_frame, text="ID DO USUARIO :", bg="#002333", fg="white").place(x=400, y=50)
        self.IdProdutoEntry = ttk.Entry(self.main_frame, width=30)
        self.IdProdutoEntry.place(x=500, y=50)

        #COMBO box fornecedor
        self.combobox_fornecedor = ctk.CTkComboBox(self.root, values= self.buscar_fornecedores(), height=30, width=210)
        self.combobox_fornecedor.place(x=600, y=100)

        # Rótulo
        label = ttk.Label(jan, text="Selecione o fornecedor:")
        label.pack(pady=10)

        # Criar o ComboBox
        combo = label(jan, values= fornecedores, state="readonly")
        combo.place(x=500, y=100)


        def buscarproduto():
            idproduto = self.IdProdutoEntry.get()
            if idproduto == "":
                messagebox.showerror(title="Erro", message="PREENCHA O CAMPO DE ID")
            else:
                db = Database()
                usuario = db.buscar_produto(idproduto)
                if usuario:
                    self.LimparCampos()
                    self.TipoProdutoEntry.insert(0, usuario[2])
                    self.VoltagemEntry.insert(0, usuario[3])
                    self.MarcaEntry.insert(0, usuario[4])
                    self.QuantidadeEntry.insert(0, usuario[5])
                    self.PrecoEntry.insert(0, usuario[6])
                    self.DataProdutoEntry.insert(0, usuario[7])
                else:
                    messagebox.showerror("Erro", "Funcionário não encontrado")
                    self.LimparCampos()

        def buscar_fornecedores():
            db = Database()
            busca = listar_fornecedores_db()
            fornecedores = [nome[1] for nome in busca]
            return fornecedores




        def alterarproduto():
            idproduto = self.IdProdutoEntry.get()
            tipo = self.TipoProdutoEntry.get()
            voltagem = self.VoltagemEntry.get()
            marca = self.MarcaEntry.get()
            quantidade = self.QuantidadeEntry.get()
            preco = self.PrecoEntry.get()
            data = self.DataProdutoEntry.get()

            if "" in [idproduto, tipo, voltagem, marca, quantidade, preco, data]:
                messagebox.showerror(title="Erro de Atualização", message="PREENCHA TODOS OS CAMPOS")
            else:
                db = Database()
                db.alterarproduto(idproduto, tipo, voltagem, marca, quantidade, preco, data)
                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")

        def excluirproduto():
            idproduto = self.IdProdutoEntry.get()
            if idproduto == "":
                messagebox.showerror(title="Erro de Busca", message="PREENCHA O CAMPO DE ID")
            else:
                db = Database()
                db.removerproduto(idproduto)
                messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")

        def RegistrarNoBanco_Produto():
            tipo = self.TipoProdutoEntry.get()
            voltagem = self.VoltagemEntry.get()
            marca = self.MarcaEntry.get()
            quantidade = self.QuantidadeEntry.get()
            preco = self.PrecoEntry.get()
            data = self.DataProdutoEntry.get()

            if "" in [tipo, voltagem, marca, quantidade, preco, data]:
                messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
            else:
                db = Database()
                db.RegistrarNoBanco_Produto(tipo, voltagem, marca, quantidade, preco, data)
                messagebox.showinfo("Sucesso", "Produto registrado com sucesso!")
                self.LimparCampos()

        # Botões
        Button(self.main_frame, text="CADASTRAR", width=15, command=RegistrarNoBanco_Produto).place(x=80, y=300)
        Button(self.main_frame, text="LIMPAR", width=15, command=self.LimparCampos).place(x=250, y=300)
        Button(self.main_frame, text="ALTERAR", width=15, command=alterarproduto).place(x=80, y=340)
        Button(self.main_frame, text="EXCLUIR", width=15, command=excluirproduto).place(x=250, y=340)
        Button(self.main_frame, text="BUSCAR", width=15, command=buscarproduto).place(x=500, y=90)
        Button(self.main_frame, text="Voltar ao menu", width=15, command=self.juntar_funcoes).place(x=500, y=370)

    def LimparCampos(self):
        self.TipoProdutoEntry.delete(0, END)
        self.VoltagemEntry.delete(0, END)
        self.MarcaEntry.delete(0, END)
        self.QuantidadeEntry.delete(0, END)
        self.PrecoEntry.delete(0, END)
        self.DataProdutoEntry.delete(0, END)
        self.IdProdutoEntry.delete(0, END)

    def voltar_menu(self):
        self.root.destroy()
        from tela_ADM import TeldACASTRO
        root = Tk()
        TeldACASTRO(root)

    def juntar_funcoes(self):
        self.LimparCampos()
        self.voltar_menu()

if __name__ == "__main__":
    jan = Tk()
    jan.title("USUARIO - PRODUTO")
    jan.geometry("800x400")
    jan.configure(background="#002333")
    jan.resizable(width=False, height=False)
    logo = PhotoImage(file="icon/_SLA_.png")
    LogoLabel = Label(image=logo, bg="#002333")
    LogoLabel.place(x=500, y=150)
    app = AbrirProduto_adm(jan)
    jan.mainloop()
