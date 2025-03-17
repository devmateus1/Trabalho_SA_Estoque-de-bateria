from tkinter import * # Importa todos os módulos do tkinter
from tkinter import messagebox # Importa o módulo de widgets temáticos do tkinter
from tkinter import ttk
from DataBase import Database

class AbrirProduto_adm:
    def __init__(self,root):
 
        Cadastrotitulo = Label (text="CADASTRO DE PRODUTO | ADM :", bg="#002333", fg="white") # Cria o titulo
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

        IdProdutoLabel = Label (text="ID DO USUARIO :", bg="#002333", fg="white")
        IdProdutoLabel.place (x=400 , y=50)
        IdProdutoEntry =ttk.Entry(width=30)
        IdProdutoEntry.place (x=500 , y=50)


        def LimparCampos():
            TipoProdutoEntry.delete(0 ,END)
            VoltagemEntry.delete(0 ,END)
            PrecoEntry.delete(0 ,END)
            DataProdutoEntry.delete (0, END)
            QuantidadeEntry.delete(0 ,END)
            PrecoEntry.delete(0 ,END)
            IdProdutoEntry.delete(0 ,END)
            MarcaEntry.delete(0 ,END)
 

        def buscarproduto():
            idproduto = IdProdutoEntry.get()
            if idproduto == "":
                messagebox.showerror(title="Erro", message="PREENCHA O CAMPO DE ID")
            else:
                db = Database()  # Crie uma instância do banco de dados
                usuario = db.buscar_produto(idproduto)  # Supondo que exista um método para buscar por id
            if usuario:
                TipoProdutoEntry.delete(0 ,END)
                VoltagemEntry.delete(0 ,END)
                PrecoEntry.delete(0 ,END)
                DataProdutoEntry.delete (0, END)
                QuantidadeEntry.delete(0 ,END)
                PrecoEntry.delete(0 ,END)

                TipoProdutoEntry.insert(0, usuario[1])
                VoltagemEntry.insert(0, usuario[2])
                MarcaEntry.insert(0, usuario[3])
                QuantidadeEntry.insert(0, usuario[4])
                PrecoEntry.insert(0, usuario[5])
                DataProdutoEntry.insert(0, usuario[6])

            else:
                messagebox.showerror("Erro", "Funcionário não encontrado")
                LimparCampos()

        def alterarproduto():
            #Transforma os campos de textos em variaveis
            idproduto=IdProdutoEntry.get()
            tipo=TipoProdutoEntry.get()
            voltagem=VoltagemEntry.get()
            marca=MarcaEntry.get()
            quantidade=QuantidadeEntry.get()
            preco=PrecoEntry.get()
            data=DataProdutoEntry.get()
            

            if idproduto =="" or tipo == "" or voltagem == "" or marca == "" or quantidade == "" or preco == "" or data == "" : #Verifica se os campos de textos estão vazios
                messagebox.showerror(title="Erro de Atulização", message="PREENCHA TODOS OS CAMPOS") #Exibe a mensagem de erro
            else:
                db = Database() #Cria uma instancia da classe Database
                db.alterarproduto(idproduto, tipo, voltagem, marca, quantidade, preco, data) #Chama o metodo para registrar no banco de dados 
                messagebox.showinfo("Sucesso","Produto atualizado com sucesso!") #Exibe a mensagem de sucesso

        def excluirproduto():
            idproduto=IdProdutoEntry.get()
            if idproduto =="": #Verifica se a caixa de texto do id está vazia
                messagebox.showerror(title="Erro de Busca", message="PREENCHA O CAMPO DE ID") #Exibe a mensagem de erro
            else:
                db = Database() #Cria uma instancia da classe Database
                db.removerproduto(idproduto)
                messagebox.showinfo("Sucesso","Produto excluido com sucesso!") #Exibe a mensagem de sucesso

                # Botão de cadastrar


 
         # Botão de limpar campos
 
        LimparCampos = Button(text="LIMPAR", width=15, command=LimparCampos)
        LimparCampos.place(x=250 , y=300)

        Alterar = Button(text="ALTERAR", width=15, command=alterarproduto)
        Alterar.place(x=80, y=340)

        Excluir = Button(text="EXCLUIR", width=15, command=excluirproduto)
        Excluir.place(x=80, y=300)

        buscarbotao = Button(text="BUSCAR", width=15,command=buscarproduto)
        buscarbotao.place (x=500 , y=90)

if __name__ == "__main__":
        jan = Tk()
        jan.title("USUARIO - PRODUTO")
        jan.geometry("800x400")
        jan.configure(background="#002333")
        jan.resizable(width=False, height=False)
        logo = PhotoImage(file="icon/_SLA_.png") # Carrega a imagem do logo
        LogoLabel = Label(image=logo, bg="#002333") # Cria um label para a imagem do logo
        LogoLabel.place(x=500, y=100) # Posiciona o label no frame esquerdo
        LogoLabel.place(x=500, y=150) # Posiciona o label no frame esquerdo
        app = AbrirProduto_adm(jan)
        jan.mainloop()