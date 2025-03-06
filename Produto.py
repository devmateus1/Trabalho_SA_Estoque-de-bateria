from tkinter import * #Importa todos os mudulos do tkinter
from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
from tkinter import ttk
#from DataBase import DataBase

def LimparCampos():
    NomeProdutoEntry.delete(0 ,END)
    VoltagemEntry.delete(0 ,END)
    MarcaEntry.delete(0 ,END)
    QuantidadeEntry.delete(0 ,END)
    PrecoEntry.delete(0 ,END)

def RegistrarNoBanco():
        nome = NomeProdutoEntry.get() # Obtém o valor do campo de entrada do nome
        Voltagem = VoltagemEntry.get() # Obtém o valor do campo de entrada do email
        Marca = MarcaEntry.get() # Obtém o valor do campo de entrada do usuario
        Quantidade = QuantidadeEntry.get() # Obtém o valordo campo de entrada da senha
        Preco = PrecoEntry.get() # Obtém o valordo campo de entrada da senha

        if nome == "" or Voltagem == "" or Marca == "" or Quantidade == "" or Preco == "":
            messagebox.showerror(title="Erro no Registro",message="PREENCHA TODOS OS CAMPOS") # Exibe mensagm de erro
        else:
           # db = DataBase() # Cria uma instância da classe Database
            #db.RegistrarNoBanco(nome, Voltagem, Marca, Quantidade, Preco) # Chama o método para registrar no banco de dados
            messagebox.showinfo("Sucesso","Usuário registrado com sucesso!") # Exibe mensagem de Sucesso

            # Limpar os campos após o registro
            NomeProdutoEntry.delete(0, END) # Limpa o campo de entrada do nome
            VoltagemEntry.delete(0, END) # Limpa o campo de entrada do email
            MarcaEntry.delete(0, END) # Limpa o campo de entrada do usuario
            QuantidadeEntry.delete(0, END) # Limpa o campo de entrada do senha
            PrecoEntry.delete(0, END) # Limpa o campo de entrada do senha

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

NomeProdutoLabel = Label (text="TIPO DA BATERIA :", bg="#002333", fg="white")
NomeProdutoLabel.place (x=55 , y=50)
NomeProdutoEntry =ttk.Entry(width=30)
NomeProdutoEntry.place (x=170 , y=50)

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

NomeProdutoLabel = Label (text="DATA DE VALIDADE :", bg="#002333", fg="white")
NomeProdutoLabel.place (x=45 , y=250)
NomeProdutoEntry =ttk.Entry(width=30)
NomeProdutoEntry.place (x=170 , y=250)

# Botão de cadastrar
Cadastrar = Button(text="CADASTRAR", width=15)
Cadastrar.place(x=80, y=320)

# Botão de limpar campos

LimparCampos = Button(text="LIMPAR", width=15, command=LimparCampos)
LimparCampos.place(x=250 , y=320)






jan.mainloop()
