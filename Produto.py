from tkinter import * #Importa todos os mudulos do tkinter
from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
from tkinter import ttk
from DatabaseProduto import DataBase


def LimparCampos():
    tipoProdutoEntry.delete(0 ,END)
    VoltagemEntry.delete(0 ,END)
    MarcaEntry.delete(0 ,END)
    QuantidadeEntry.delete(0 ,END)
    PrecoEntry.delete(0 ,END)
    dataProdutoEntry.delete (0, END)

def RegistrarNoBanco():
    tipo = tipoProdutoEntry.get() # Obtém o valor do campo de entrada do tipo do produto
    Voltagem = VoltagemEntry.get() # Obtém o valor do campo de entrada da voltagem do produto
    Marca = MarcaEntry.get() # Obtém o valor do campo de entrada da marca do produto
    Quantidade = QuantidadeEntry.get() # Obtém o valor do campo de entrada da quantidade do produto
    Preco = PrecoEntry.get() #Obtém o valor do campo de entrada da quantidade do produto
    Data = dataProdutoEntry.get() # Obtém o valor do campo de entrada da quantidade do produto

    if tipo == "" or Voltagem == "" or Marca == "" or Quantidade == "" or Preco == "" or Data == "":
         messagebox.showerror(title="Erro no Registro",message="PREENCHA TODOS OS CAMPOS") # Exibe mensagm de erro
    else:
        db = DataBase() # Cria uma instância da classe Database
        db.RegistrarNoBanco(tipo, Voltagem, Marca, Quantidade, Preco, Data) # Chama o método para registrar no banco de dados
        messagebox.showinfo("Sucesso","Usuário registrado com sucesso!") # Exibe mensagem de Sucesso

            # Limpar os campos após o registro
        tipoProdutoEntry.delete(0, END) # Limpa o campo de entrada do tipo
        VoltagemEntry.delete(0, END) # Limpa o campo de entrada da voltagem
        MarcaEntry.delete(0, END) # Limpa o campo de entrada da marca
        QuantidadeEntry.delete(0, END) # Limpa o campo de entrada da quantidade
        PrecoEntry.delete(0, END) # Limpa o campo de entrada do preço
        dataProdutoEntry.delete(0, END) # Limpa o campo de entrada da data


# Criar a janela
jan = Tk()
jan.title("USUARIO - PRODUTO")
jan.geometry("800x400")
jan.configure(background="#002333")
jan.resizable(width=False, height=False)


logo = PhotoImage(file="icon/_SLA_.png") # Carrega a imagem do logo
LogoLabel = Label(image=logo, bg="#002333") # Cria um label para a imagem do logo
LogoLabel.place(x=500, y=100) # Posiciona o label no frame esquerdo

Cadastrotitulo = Label (text="CADASTRO DE PRODUTO :", bg="#002333", fg="white") # Cria o titulo
Cadastrotitulo.place(x=230 , y=10) # Posiciona o titulo

# CRIAÇÃO DOS LABELS E CAMPOS DE ENTRADAS
# POSIONAMENTO DOS LABELS E DOS CAMPOS DE ENTRADAS

tipoProdutoLabel = Label (text="TIPO DA BATERIA :", bg="#002333", fg="white")
tipoProdutoLabel.place (x=55 , y=50)
tipoProdutoEntry =ttk.Entry(width=30)
tipoProdutoEntry.place (x=170 , y=50)

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

dataProdutoLabel = Label (text="DATA DE VALIDADE :", bg="#002333", fg="white")
dataProdutoLabel.place (x=45 , y=250)
dataProdutoEntry =ttk.Entry(width=30)
dataProdutoEntry.place (x=170 , y=250)

# Botão de cadastrar
Cadastrar = Button(text="CADASTRAR", width=15, command=RegistrarNoBanco)
Cadastrar.place(x=80, y=320)

# Botão de limpar campos

LimparCampos = Button(text="LIMPAR", width=15, command=LimparCampos)
LimparCampos.place(x=250 , y=320)

#Continuar = Button(text="CONTINUAR", width=15, command=)






jan.mainloop()
