from tkinter import * # Importa todos os módulos do tkinter
from tkinter import messagebox # Importa o módulo de widgets temáticos do tkinter
from tkinter import ttk
from DataBase import Database

class AbrirProduto_cadastro:
    def __init__(self,root):
 
        Cadastrotitulo = Label (text="CADASTRO DE PRODUTO | CADASTRO :", bg="#002333", fg="white") # Cria o titulo
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
        


        def LimparCampos():
            TipoProdutoEntry.delete(0 ,END)
            VoltagemEntry.delete(0 ,END)
            PrecoEntry.delete(0 ,END)
            DataProdutoEntry.delete (0, END)
            QuantidadeEntry.delete(0 ,END)
            PrecoEntry.delete(0 ,END)
            MarcaEntry.delete(0 ,END)
 
 
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


        Cadastrar = Button(text="CADASTRAR", width=15, command=RegistrarNoBanco_Produto)
        Cadastrar.place(x=80, y=300)
 
         # Botão de limpar campos
 
        LimparCampos = Button(text="LIMPAR", width=15, command=LimparCampos)
        LimparCampos.place(x=250 , y=300)



if __name__ == "__main__":
        jan = Tk()
        jan.title("USUARIO - PRODUTO")
        jan.geometry("800x400")
        jan.configure(background="#002333")
        jan.resizable(width=False, height=False)
        logo = PhotoImage(file="icon/_SLA_.png") # Carrega a imagem do logo
        LogoLabel = Label(image=logo, bg="#002333") # Cria um label para a imagem do logo
        LogoLabel.place(x=500, y=100) # Posiciona o label no frame esquerdo
        app = AbrirProduto_cadastro(jan)
        jan.mainloop()
