from tkinter import * # Importa todos os módulos do tkinter
from tkinter import messagebox # Importa o módulo de widgets temáticos do tkinter
from tkinter import ttk
<<<<<<< Updated upstream
from DataBase import Database
=======
from DatabaseProduto import DataBase

<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
class AbrirProduto:
    def __init__(self, master):
        self.master = master  # Armazena a referência para a janela principal
        self.master.title("USUARIO - PRODUTO")
        self.master.geometry("800x400")
        self.master.configure(background="#002333")
        self.master.resizable(width=False, height=False)
<<<<<<< Updated upstream

<<<<<<< Updated upstream
        Cadastrotitulo = Label (text="CADASTRO DE PRODUTO :", bg="#002333", fg="white") # Cria o titulo
        Cadastrotitulo.place(x=230 , y=10) # Posiciona o titulo

        # CRIAÇÃO DOS LABELS E CAMPOS DE ENTRADAS
        # POSIONAMENTO DOS LABELS E DOS CAMPOS DE ENTRADAS


        TipoProdutoLabel = Label (text="TIPO DA BATERIA :", bg="#002333", fg="white")
        TipoProdutoLabel.place (x=55 , y=50)
        TipoProdutoEntry =ttk.Entry(width=30)
        TipoProdutoEntry.place (x=170 , y=50)

        VoltagemLabel = Label (text="VOLTAGEM DA BATERIA :", bg="#002333", fg="white")
        VoltagemLabel.place (x=20 , y=90)
        VoltagemEntry =ttk.Entry(width=30)
        VoltagemEntry.place (x=170 , y=90)

        MarcaLabel = Label (text="MARCA DA BATERIA :", bg="#002333", fg="white")
        MarcaLabel.place (x=40 , y=130)
        MarcaEntry =ttk.Entry(width=30)
        MarcaEntry.place (x=170 , y=130)

        QuantidadeLabel = Label (text="QUANTIDADE DA BATERIA :", bg="#002333", fg="white")
        QuantidadeLabel.place (x=8 , y=170)
        QuantidadeEntry =ttk.Entry(width=30)
        QuantidadeEntry.place (x=170 , y=170)

        PrecoLabel = Label (text="PREÇO DA BATERIA :", bg="#002333", fg="white")
        PrecoLabel.place (x=45 , y=210)
        PrecoEntry =ttk.Entry(width=30)
        PrecoEntry.place (x=170 , y=210)

        DataBaseataProdutoLabel = Label (text="DATA DE VALIDADE :", bg="#002333", fg="white")
        DataBaseataProdutoLabel.place (x=45 , y=250)
        DataProdutoEntry =ttk.Entry(width=30)
        DataProdutoEntry.place (x=170 , y=250)
=======
        # Criação do título
        self.Cadastrotitulo = Label(self.master, text="CADASTRO DE PRODUTO :", bg="#002333", fg="white")
        self.Cadastrotitulo.place(x=230, y=10)

        # Criação dos Labels e campos de entrada
        self.TipoProdutoLabel = Label(self.master, text="TIPO DA BATERIA :", bg="#002333", fg="white")
        self.TipoProdutoLabel.place(x=55, y=50)
        self.TipoProdutoEntry = ttk.Entry(self.master, width=30)
        self.TipoProdutoEntry.place(x=170, y=50)

        self.VoltagemLabel = Label(self.master, text="VOLTAGEM DA BATERIA :", bg="#002333", fg="white")
        self.VoltagemLabel.place(x=20, y=90)
        self.VoltagemEntry = ttk.Entry(self.master, width=30)
        self.VoltagemEntry.place(x=170, y=90)

        self.MarcaLabel = Label(self.master, text="MARCA DA BATERIA :", bg="#002333", fg="white")
        self.MarcaLabel.place(x=40, y=130)
        self.MarcaEntry = ttk.Entry(self.master, width=30)
        self.MarcaEntry.place(x=170, y=130)

        self.QuantidadeLabel = Label(self.master, text="QUANTIDADE DA BATERIA :", bg="#002333", fg="white")
        self.QuantidadeLabel.place(x=8, y=170)
        self.QuantidadeEntry = ttk.Entry(self.master, width=30)
        self.QuantidadeEntry.place(x=170, y=170)

        self.PrecoLabel = Label(self.master, text="PREÇO DA BATERIA :", bg="#002333", fg="white")
        self.PrecoLabel.place(x=45, y=210)
        self.PrecoEntry = ttk.Entry(self.master, width=30)
        self.PrecoEntry.place(x=170, y=210)

=======

        # Criação do título
        self.Cadastrotitulo = Label(self.master, text="CADASTRO DE PRODUTO :", bg="#002333", fg="white")
        self.Cadastrotitulo.place(x=230, y=10)

        # Criação dos Labels e campos de entrada
        self.TipoProdutoLabel = Label(self.master, text="TIPO DA BATERIA :", bg="#002333", fg="white")
        self.TipoProdutoLabel.place(x=55, y=50)
        self.TipoProdutoEntry = ttk.Entry(self.master, width=30)
        self.TipoProdutoEntry.place(x=170, y=50)

        self.VoltagemLabel = Label(self.master, text="VOLTAGEM DA BATERIA :", bg="#002333", fg="white")
        self.VoltagemLabel.place(x=20, y=90)
        self.VoltagemEntry = ttk.Entry(self.master, width=30)
        self.VoltagemEntry.place(x=170, y=90)

        self.MarcaLabel = Label(self.master, text="MARCA DA BATERIA :", bg="#002333", fg="white")
        self.MarcaLabel.place(x=40, y=130)
        self.MarcaEntry = ttk.Entry(self.master, width=30)
        self.MarcaEntry.place(x=170, y=130)

        self.QuantidadeLabel = Label(self.master, text="QUANTIDADE DA BATERIA :", bg="#002333", fg="white")
        self.QuantidadeLabel.place(x=8, y=170)
        self.QuantidadeEntry = ttk.Entry(self.master, width=30)
        self.QuantidadeEntry.place(x=170, y=170)

        self.PrecoLabel = Label(self.master, text="PREÇO DA BATERIA :", bg="#002333", fg="white")
        self.PrecoLabel.place(x=45, y=210)
        self.PrecoEntry = ttk.Entry(self.master, width=30)
        self.PrecoEntry.place(x=170, y=210)

>>>>>>> Stashed changes
        self.DataProdutoLabel = Label(self.master, text="DATA DE VALIDADE :", bg="#002333", fg="white")
        self.DataProdutoLabel.place(x=45, y=250)
        self.DataProdutoEntry = ttk.Entry(self.master, width=30)
        self.DataProdutoEntry.place(x=170, y=250)
<<<<<<< Updated upstream
>>>>>>> Stashed changes

        def LimparCampos():
            TipoProdutoEntry.delete(0 ,END)
            VoltagemEntry.delete(0 ,END)
            MarcaEntry.delete(0 ,END)
            QuantidadeEntry.delete(0 ,END)
            PrecoEntry.delete(0 ,END)
            DataProdutoEntry.delete (0, END)


        def RegistrarNoBanco_Produto():
            tipo = TipoProdutoEntry.get() # Obtém o valor do campo de entrada do tipo do produto
            voltagem = VoltagemEntry.get() # Obtém o valor do campo de entrada da voltagem do produto
            marca = MarcaEntry.get() # Obtém o valor do campo de entrada da marca do produto
            quantidade = QuantidadeEntry.get() # Obtém o valor do campo de entrada da quantidade do produto
            preco = PrecoEntry.get() #Obtém o valor do campo de entrada da quantidade do produto
            data = DataProdutoEntry.get() # Obtém o valor do campo de entrada da quantidade do produto

            if tipo == "" or voltagem == "" or marca == "" or quantidade == "" or preco == "" or data == "":
                messagebox.showerror(title="Erro no Registro",message="PREENCHA TODOS OS CAMPOS") # Exibe mensagm de erro
            else:
                db = Database() # Cria uma instância da classe Database
                db.RegistrarNoBanco_Produto(tipo, voltagem, marca, quantidade, preco, data) # Chama o método para registrar no banco de dados
                messagebox.showinfo("Sucesso","Usuário registrado com sucesso!") # Exibe mensagem de Sucesso

                    # Limpar os campos após o registro
                TipoProdutoEntry.delete(0, END) # Limpa o campo de entrada do tipo
                VoltagemEntry.delete(0, END) # Limpa o campo de entrada da voltagem
                MarcaEntry.delete(0, END) # Limpa o campo de entrada da marca
                QuantidadeEntry.delete(0, END) # Limpa o campo de entrada da quantidade
                PrecoEntry.delete(0, END) # Limpa o campo de entrada do preço
                DataProdutoEntry.delete(0, END) # Limpa o campo de entrada da data



        Cadastrotitulo = Label (text="CADASTRO DE PRODUTO :", bg="#002333", fg="white") # Cria o titulo
        Cadastrotitulo.place(x=230 , y=10) # Posiciona o titulo



        # Botão de cadastrar
<<<<<<< Updated upstream
        Cadastrar = Button(text="CADASTRAR", width=15, command=RegistrarNoBanco_Produto)
        Cadastrar.place(x=80, y=320)
=======
        self.Cadastrar = Button(self.master, text="CADASTRAR", width=15, command=self.RegistrarNoBancos)
        self.Cadastrar.place(x=80, y=320)
>>>>>>> Stashed changes
=======

        # Botão de cadastrar
        self.Cadastrar = Button(self.master, text="CADASTRAR", width=15, command=self.RegistrarNoBancos)
        self.Cadastrar.place(x=80, y=320)
>>>>>>> Stashed changes

        # Botão de limpar campos
        self.LimparCampos = Button(self.master, text="LIMPAR", width=15, command=self.LimparCampos)
        self.LimparCampos.place(x=250, y=320)
<<<<<<< Updated upstream

        # Carregar o logo
        self.logo = PhotoImage(file="icon/_SLA_.png")  # Carrega a imagem do logo
        self.LogoLabel = Label(self.master, image=self.logo, bg="#002333")  # Cria um label para a imagem do logo
        self.LogoLabel.place(x=500, y=100)  # Posiciona o label no frame esquerdo

    def LimparCampos(self):
        """Limpa os campos de entrada"""
        self.TipoProdutoEntry.delete(0, END)
        self.VoltagemEntry.delete(0, END)
        self.MarcaEntry.delete(0, END)
        self.QuantidadeEntry.delete(0, END)
        self.PrecoEntry.delete(0, END)
        self.DataProdutoEntry.delete(0, END)

    def RegistrarNoBancos(self):
        """Registra o produto no banco de dados"""
        tipo = self.TipoProdutoEntry.get()
        voltagem = self.VoltagemEntry.get()
        marca = self.MarcaEntry.get()
        quantidade = self.QuantidadeEntry.get()
        preco = self.PrecoEntry.get()
        data = self.DataProdutoEntry.get()

        # Verifica se todos os campos foram preenchidos
        if tipo == "" or voltagem == "" or marca == "" or quantidade == "" or preco == "" or data == "":
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            db = DataBase()  # Cria uma instância da classe Database
            db.RegistrarNoBanco(tipo, voltagem, marca, quantidade, preco, data)  # Registra no banco de dados
            messagebox.showinfo("Sucesso", "Produto registrado com sucesso!")  # Exibe mensagem de sucesso

            # Limpar os campos após o registro
            self.LimparCampos()



if __name__ == "__main__":
<<<<<<< Updated upstream
        jan = Tk()
        jan.title("USUARIO - PRODUTO")
        jan.geometry("800x400")
        jan.configure(background="#002333")
        jan.resizable(width=False, height=False)
        logo = PhotoImage(file="icon/_SLA_.png") # Carrega a imagem do logo
        LogoLabel = Label(image=logo, bg="#002333") # Cria um label para a imagem do logo
        LogoLabel.place(x=500, y=150) # Posiciona o label no frame esquerdo
        app = AbrirProduto(jan)
        jan.mainloop()
=======
    jan = Tk()
    app = AbrirProduto(jan)  # Cria uma instância da classe AbrirProduto
    jan.mainloop()
>>>>>>> Stashed changes
=======

        # Carregar o logo
        self.logo = PhotoImage(file="icon/_SLA_.png")  # Carrega a imagem do logo
        self.LogoLabel = Label(self.master, image=self.logo, bg="#002333")  # Cria um label para a imagem do logo
        self.LogoLabel.place(x=500, y=100)  # Posiciona o label no frame esquerdo

    def LimparCampos(self):
        """Limpa os campos de entrada"""
        self.TipoProdutoEntry.delete(0, END)
        self.VoltagemEntry.delete(0, END)
        self.MarcaEntry.delete(0, END)
        self.QuantidadeEntry.delete(0, END)
        self.PrecoEntry.delete(0, END)
        self.DataProdutoEntry.delete(0, END)

    def RegistrarNoBancos(self):
        """Registra o produto no banco de dados"""
        tipo = self.TipoProdutoEntry.get()
        voltagem = self.VoltagemEntry.get()
        marca = self.MarcaEntry.get()
        quantidade = self.QuantidadeEntry.get()
        preco = self.PrecoEntry.get()
        data = self.DataProdutoEntry.get()

        # Verifica se todos os campos foram preenchidos
        if tipo == "" or voltagem == "" or marca == "" or quantidade == "" or preco == "" or data == "":
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            db = DataBase()  # Cria uma instância da classe Database
            db.RegistrarNoBanco(tipo, voltagem, marca, quantidade, preco, data)  # Registra no banco de dados
            messagebox.showinfo("Sucesso", "Produto registrado com sucesso!")  # Exibe mensagem de sucesso

            # Limpar os campos após o registro
            self.LimparCampos()


if __name__ == "__main__":
    jan = Tk()
    app = AbrirProduto(jan)  # Cria uma instância da classe AbrirProduto
    jan.mainloop()
>>>>>>> Stashed changes
