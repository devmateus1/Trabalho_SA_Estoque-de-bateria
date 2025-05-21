from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database

class AbrirProduto_adm:
    def __init__(self, root):
        self.root = root
        self.main_frame = Frame(self.root, bg="#002333")
        self.main_frame.pack(expand=True, fill=BOTH)

        Label(self.main_frame, text="CADASTRO DE PRODUTO | ADM :", bg="#002333", fg="white").place(x=230, y=10)

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

        Label(self.main_frame, text="ID DO PRODUTO :", bg="#002333", fg="white").place(x=400, y=50)
        self.IdProdutoEntry = ttk.Entry(self.main_frame, width=30)
        self.IdProdutoEntry.place(x=500, y=50)

        Label(self.main_frame, text="Fornecedor:", bg="#002333", fg="white").place(x=400, y=130)
        db = Database()
        fornecedores = db.buscar_nome_fornecedor()
        self.combo_box_forn = ttk.Combobox(self.main_frame, values=fornecedores, state="readonly", width=27)
        self.combo_box_forn.place(x=500, y=130)
        self.combo_box_forn.set("Selecione um fornecedor")

        # Botões
        Button(self.main_frame, text="CADASTRAR", width=15, command=self.RegistrarNoBanco_Produto).place(x=80, y=300)
        Button(self.main_frame, text="LIMPAR", width=15, command=self.LimparCampos).place(x=250, y=300)
        Button(self.main_frame, text="ALTERAR", width=15, command=self.alterarproduto).place(x=80, y=340)
        Button(self.main_frame, text="EXCLUIR", width=15, command=self.excluirproduto).place(x=250, y=340)
        Button(self.main_frame, text="BUSCAR", width=15, command=self.buscarproduto).place(x=500, y=90)
        Button(self.main_frame, text="Voltar ao menu", width=15, command=self.juntar_funcoes).place(x=650, y=90)

    def LimparCampos(self):
        self.TipoProdutoEntry.delete(0, END)
        self.VoltagemEntry.delete(0, END)
        self.MarcaEntry.delete(0, END)
        self.QuantidadeEntry.delete(0, END)
        self.PrecoEntry.delete(0, END)
        self.DataProdutoEntry.delete(0, END)
        self.IdProdutoEntry.delete(0, END)
        self.combo_box_forn.set("Selecione um fornecedor")

    def voltar_menu(self):
        self.root.destroy()
        from tela_ADM import TelaCadastro
        root = Tk()
        TelaCadastro(root)

    def juntar_funcoes(self):
        self.LimparCampos()
        self.voltar_menu()

    def extrair_id_combobox(self, fornecedor_str):
        partes = fornecedor_str.split()
        for parte in partes:
            if parte.isdigit():
                return int(parte)
        return None

    def buscarproduto(self):
        idproduto = self.IdProdutoEntry.get()
        if idproduto == "":
            messagebox.showerror("Erro", "PREENCHA O CAMPO DE ID")
            return

        db = Database()
        usuario = db.buscar_produto(idproduto)
        if usuario:
            self.TipoProdutoEntry.delete(0, END)
            self.VoltagemEntry.delete(0, END)
            self.MarcaEntry.delete(0, END)
            self.QuantidadeEntry.delete(0, END)
            self.PrecoEntry.delete(0, END)
            self.DataProdutoEntry.delete(0, END)

            self.TipoProdutoEntry.insert(0, usuario[2])
            self.VoltagemEntry.insert(0, usuario[3])
            self.MarcaEntry.insert(0, usuario[4])
            self.QuantidadeEntry.insert(0, usuario[5])
            self.PrecoEntry.insert(0, usuario[6])
            self.DataProdutoEntry.insert(0, usuario[7])
            self.combo_box_forn.set(usuario[9])  # nome do fornecedor
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
        fornecedor = self.combo_box_forn.get()

        if "" in [idproduto, tipo, voltagem, marca, quantidade, preco, data, fornecedor]:
            messagebox.showerror("Erro", "PREENCHA TODOS OS CAMPOS")
            return

        cod_fornecedor = self.extrair_id_combobox(fornecedor)
        if cod_fornecedor is None:
            messagebox.showerror("Erro", "Fornecedor inválido")
            return

        try:
            db = Database()
            db.alterarproduto(idproduto, tipo, voltagem, marca, quantidade, preco, data, cod_fornecedor)
            messagebox.showinfo("Sucesso", "Produto alterado com sucesso!")
            self.LimparCampos()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao alterar produto: {str(e)}")

    def excluirproduto(self):
        idproduto = self.IdProdutoEntry.get()
        if idproduto == "":
            messagebox.showerror("Erro", "PREENCHA O CAMPO DE ID")
            return

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
        fornecedor = self.combo_box_forn.get()

        if "" in [tipo, voltagem, marca, quantidade, preco, data] or fornecedor == "Selecione um fornecedor":
            messagebox.showerror("Erro", "PREENCHA TODOS OS CAMPOS")
            return

        cod_fornecedor = self.extrair_id_combobox(fornecedor)
        if cod_fornecedor is None:
            messagebox.showerror("Erro", "Fornecedor inválido")
            return

        db = Database()
        db.RegistrarNoBanco_Produto(tipo, voltagem, marca, quantidade, preco, data, cod_fornecedor)
        messagebox.showinfo("Sucesso", "Produto registrado com sucesso!")
        self.LimparCampos()
    
    def voltar_menu(self):
        self.root.destroy()
        from tela_ADM import TeldACASTRO
        root = Tk()
        TeldACASTRO(root)

# Execução principal
if __name__ == "__main__":
    jan = Tk()
    jan.title("USUARIO - PRODUTO")
    jan.geometry("800x400")
    jan.configure(background="#002333")
    jan.resizable(width=False, height=False)
    app = AbrirProduto_adm(jan)

    logo = PhotoImage(file="icon/_SLA_.png")
    LogoLabel = Label(image=logo, bg="#002333")
    LogoLabel.place(x=480, y=180)

    jan.mainloop()
