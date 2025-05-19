from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database

class Abrir_pedido:
    def __init__(self, root):
        self.root = root
        self.root.title("ADM - Fazer pedido")
        self.root.geometry("700x500")
        self.root.configure(bg="#002333")
        self.root.resizable(width=False, height=False)

        try:
            self.logo = PhotoImage(file="icon/_SLA_.png")
            LogoLabel = Label(self.root, image=self.logo, bg="#002333")
            LogoLabel.place(x=390,y=70)
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

        self.criar_widgets()

    def criar_widgets(self):
        Label(self.root, text="Fazer pedido:", bg="#002333", fg="white", font=("Arial", 14)).place(x=160, y=10)

        Label(self.root, text="Id do Cliente:", bg="#002333", fg="white").place(x=10, y=80)
        self.idclienteEntry = ttk.Entry(self.root, width=30)
        self.idclienteEntry.place(x=150, y=80)

        Label(self.root, text="Id do funcionario:", bg="#002333", fg="white").place(x=10, y=120)
        self.IdfuncionarioEntry = ttk.Entry(self.root, width=30)
        self.IdfuncionarioEntry.place(x=150, y=120)

        Label(self.root, text="Data da compra:", bg="#002333", fg="white").place(x=10, y=160)
        self.dataEntry = ttk.Entry(self.root, width=30)
        self.dataEntry.place(x=150, y=160)

        Label(self.root, text="Id da compra:", bg="#002333", fg="white").place(x=10, y=200)
        self.idEntry = ttk.Entry(self.root, width=30)
        self.idEntry.place(x=150, y=200)

        ttk.Button(self.root, text="Cadastrar", width=15, command=self.RegistrarNoBancocompra).place(x=130, y=230)
        ttk.Button(text="LIMPAR", width=15, command=self.limpar_campos).place(x=250, y=230)

    def RegistrarNoBancocompra(self):
        idcompra = self.idEntry.get()
        idcliente = self.idclienteEntry.get()
        idfuncionario = self.IdfuncionarioEntry.get()
        data_compra = self.idEntry.get()

        if "" in [idcliente, idfuncionario, data_compra, idcompra]:
            messagebox.showerror("Erro de Cadastro", "PREENCHA TODOS OS CAMPOS")
        else:
            db = Database()
            db.RegistrarNoBancoCompra(idcliente, idfuncionario, data_compra, idcompra)
            messagebox.showinfo("Sucesso", "Fornecedor registrado com sucesso!")

    def limpar_campos(self):
        self.TipoProdutoEntry.delete(0, END)
        self.QuantidadeEntry.delete(0, END)
        self.PrecoEntry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = Abrir_pedido(root)
    root.mainloop()
