from tkinter import *  # Importa todos os módulos do tkinter
from tkinter import messagebox, ttk
from DataBase import Database


class AbrirProduto_adm:
    def __init__(self, root):
        self.root = root
        self.root.title("CADASTRO DE PRODUTO | ADM")
        self.root.geometry("800x400")
        self.root.configure(background="#002333")
        self.root.resizable(width=False, height=False)

        # Carrega o logo
        try:
            self.logo = PhotoImage(file="icon/_SLA_.png")  # Caminho relativo da imagem
            self.logo_label = Label(self.root, image=self.logo, bg="#002333")
            self.logo_label.place(x=500, y=150)  # Posição do logo
        except Exception as e:
            messagebox.showerror("Erro ao carregar imagem", f"Não foi possível carregar o logo:\n{e}")

        # Título
        Cadastrotitulo = Label(self.root, text="CADASTRO DE PRODUTO | ADM", bg="#002333", fg="white", font=("Helvetica", 16))
        Cadastrotitulo.place(x=230, y=10)

        # CRIAÇÃO DOS CAMPOS
        TipoProdutoLabel = Label(self.root, text="TIPO DA BATERIA:", bg="#002333", fg="white")
        TipoProdutoLabel.place(x=55, y=50)
        self.TipoProdutoEntry = ttk.Entry(self.root, width=30)
        self.TipoProdutoEntry.place(x=170, y=50)

        VoltagemLabel = Label(self.root, text="VOLTAGEM DA BATERIA:", bg="#002333", fg="white")
        VoltagemLabel.place(x=20, y=90)
        self.VoltagemEntry = ttk.Entry(self.root, width=30)
        self.VoltagemEntry.place(x=170, y=90)

        MarcaLabel = Label(self.root, text="MARCA DA BATERIA:", bg="#002333", fg="white")
        MarcaLabel.place(x=40, y=130)
        self.MarcaEntry = ttk.Entry(self.root, width=30)
        self.MarcaEntry.place(x=170, y=130)

        QuantidadeLabel = Label(self.root, text="QUANTIDADE DA BATERIA:", bg="#002333", fg="white")
        QuantidadeLabel.place(x=8, y=170)
        self.QuantidadeEntry = ttk.Entry(self.root, width=30)
        self.QuantidadeEntry.place(x=170, y=170)

        PrecoLabel = Label(self.root, text="PREÇO DA BATERIA:", bg="#002333", fg="white")
        PrecoLabel.place(x=45, y=210)
        self.PrecoEntry = ttk.Entry(self.root, width=30)
        self.PrecoEntry.place(x=170, y=210)

        DataProdutoLabel = Label(self.root, text="DATA DE VALIDADE:", bg="#002333", fg="white")
        DataProdutoLabel.place(x=45, y=250)
        self.DataProdutoEntry = ttk.Entry(self.root, width=30)
        self.DataProdutoEntry.place(x=170, y=250)

        IdProdutoLabel = Label(self.root, text="ID DO USUÁRIO:", bg="#002333", fg="white")
        IdProdutoLabel.place(x=400, y=50)
        self.IdProdutoEntry = ttk.Entry(self.root, width=30)
        self.IdProdutoEntry.place(x=500, y=50)

        # Botões
        LimparCamposBtn = Button(self.root, text="LIMPAR", width=15, command=self.LimparCampos)
        LimparCamposBtn.place(x=250, y=300)

        AlterarBtn = Button(self.root, text="ALTERAR", width=15, command=self.alterarproduto)
        AlterarBtn.place(x=80, y=340)

        ExcluirBtn = Button(self.root, text="EXCLUIR", width=15, command=self.excluirproduto)
        ExcluirBtn.place(x=250, y=340)

        CadastrarBtn = Button(self.root, text="CADASTRAR", width=15, command=self.RegistrarNoBanco_Produto)
        CadastrarBtn.place(x=80, y=300)

        BuscarBtn = Button(self.root, text="BUSCAR", width=15, command=self.buscarproduto)
        BuscarBtn.place(x=500, y=90)

    def LimparCampos(self):
        self.TipoProdutoEntry.delete(0, END)
        self.VoltagemEntry.delete(0, END)
        self.MarcaEntry.delete(0, END)
        self.QuantidadeEntry.delete(0, END)
        self.PrecoEntry.delete(0, END)
        self.DataProdutoEntry.delete(0, END)
        self.IdProdutoEntry.delete(0, END)

    def buscarproduto(self):
        idproduto = self.IdProdutoEntry.get()
        if idproduto == "":
            messagebox.showerror(title="Erro", message="PREENCHA O CAMPO DE ID")
        else:
            db = Database()
            usuario = db.buscar_produto(idproduto)
            if usuario:
                self.TipoProdutoEntry.delete(0, END)
                self.VoltagemEntry.delete(0, END)
                self.MarcaEntry.delete(0, END)
                self.QuantidadeEntry.delete(0, END)
                self.PrecoEntry.delete(0, END)
                self.DataProdutoEntry.delete(0, END)

                self.TipoProdutoEntry.insert(0, usuario[1])
                self.VoltagemEntry.insert(0, usuario[2])
                self.MarcaEntry.insert(0, usuario[3])
                self.QuantidadeEntry.insert(0, usuario[4])
                self.PrecoEntry.insert(0, usuario[5])
                self.DataProdutoEntry.insert(0, usuario[6])
            else:
                messagebox.showerror("Erro", "Produto não encontrado")
                self.LimparCampos()

    def alterarproduto(self):
        idproduto = self.IdProdutoEntry.get()
        tipo = self.TipoProdutoEntry.get()
        voltagem = self.VoltagemEntry.get()
        marca = self.MarcaEntry.get()
        quantidade = self.QuantidadeEntry.get()
        preco = self.PrecoEntry.get()
        data = self.DataProdutoEntry.get()

        if not all([idproduto, tipo, voltagem, marca, quantidade, preco, data]):
            messagebox.showerror("Erro", "Preencha todos os campos")
        else:
            db = Database()
            db.alterarproduto(idproduto, tipo, voltagem, marca, quantidade, preco, data)
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")

    def excluirproduto(self):
        idproduto = self.IdProdutoEntry.get()
        if idproduto == "":
            messagebox.showerror("Erro", "Preencha o campo de ID")
        else:
            db = Database()
            db.removerproduto(idproduto)
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
            self.LimparCampos()

    def RegistrarNoBanco_Produto(self):
        tipo = self.TipoProdutoEntry.get()
        voltagem = self.VoltagemEntry.get()
        marca = self.MarcaEntry.get()
        quantidade = self.QuantidadeEntry.get()
        preco = self.PrecoEntry.get()
        data = self.DataProdutoEntry.get()

        if not all([tipo, voltagem, marca, quantidade, preco, data]):
            messagebox.showerror("Erro", "Preencha todos os campos")
        else:
            db = Database()
            db.RegistrarNoBanco_Produto(tipo, voltagem, marca, quantidade, preco, data)
            messagebox.showinfo("Sucesso", "Produto registrado com sucesso!")
            self.LimparCampos()


# Para testar diretamente
if __name__ == "__main__":
    jan = Tk()
    app = AbrirProduto_adm(jan)
    jan.mainloop()