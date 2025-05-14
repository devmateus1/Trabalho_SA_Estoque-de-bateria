from tkinter import * #Importa todos os mudulos do tkinter
from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
from tkinter import ttk
from DataBase import Database
import tkinter as tk

class AbrirProduto_cliente:
    def __init__(self,root):

        Cadastrotitulo = Label (text="CADASTRO DE PRODUTO | CLIENTE :", bg="#002333", fg="white") # Cria o titulo
        Cadastrotitulo.place(x=230 , y=10) # Posiciona o titulo

        IdProdutoLabel = Label (text="ID DO USUARIO :", bg="#002333", fg="white")
        IdProdutoLabel.place (x=400 , y=50)
        IdProdutoEntry =ttk.Entry(width=30)
        IdProdutoEntry.place (x=500 , y=50)

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
            MarcaEntry.delete(0 ,END)
            QuantidadeEntry.delete(0 ,END)
            PrecoEntry.delete(0 ,END)
            DataProdutoEntry.delete (0, END)
            IdProdutoEntry.delete (0, END)


        def buscarproduto():
            idproduto = IdProdutoEntry.get()
            if idproduto == "":
                messagebox.showerror(title="Erro", message="PREENCHA O CAMPO DE ID")
            else:
                db = Database()  # Crie uma instância do banco de dados
                usuario = db.buscar_produto(idproduto)  # Supondo que exista um método para buscar por id
                if usuario:
                    TipoProdutoEntry.insert(0, usuario[1])
                    VoltagemEntry.insert(0, usuario[2])
                    MarcaEntry.insert(0, usuario[3])
                    QuantidadeEntry.insert(0, usuario[4])
                    PrecoEntry.insert(0, usuario[5])
                    DataProdutoEntry.insert(0, usuario[6])

                else:
                    messagebox.showerror("Erro", "Funcionário não encontrado")
                    LimparCampos()


        buscarbotao = Button(text="BUSCAR", width=15,command=buscarproduto)
        buscarbotao.place (x=500 , y=90)

        buscarbotao = Button(text="Limpar campos", width=15,command=LimparCampos)
        buscarbotao.place (x=650 , y=90)


if __name__ == "__main__":
        jan = Tk()
        jan.title("USUARIO - PRODUTO - CLIENTE")
        jan.geometry("800x400")
        jan.configure(background="#002333")
        jan.resizable(width=False, height=False)

        app = AbrirProduto_cliente(jan)
        jan.mainloop()



 

