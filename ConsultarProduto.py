from tkinter import * #Importa todos os mudulos do tkinter
from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
from tkinter import ttk
from DataBase import Database
import tkinter as tk
import mysql.connector



def __init__(self):
        #Conecta ao banco de dados MySQL com as credenciais forncedas
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'trabalho_sa'
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute()

jan = Tk()
jan.title("USUARIO - PRODUTO")
jan.geometry("800x400")
jan.configure(background="#002333")
jan.resizable(width=False, height=False)

Cadastrotitulo = Label (text="CADASTRO DE PRODUTO | ADM :", bg="#002333", fg="white") # Cria o titulo
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

def selectUser(self, idproduto):
        db = Database()
        try:
            c = db.conn.cursor()
            c.execute("SELECT * FROM produto WHERE idproduto=%s", (idproduto,))
            produto = c.fetchone()
            if produto:
                self.idusuario, self.tipo, self.voltagem, self.marca, self.quantidade, self.preco, self.data = produto
            c.close()
            return "Busca feita com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na busca do usuário: {e}"


def buscarUsuario(self,idproduto):
    idproduto = idproduto.get()
    self.cnnexecute("SELECT * FROM produto WHERE idproduto=%s", (idproduto,))
    produto = self.cursor.fetchone()
    if produto:
        TipoProdutoEntry.insert(0, produto[1])
        VoltagemEntry.insert(0, produto[2])
        MarcaEntry.insert(0, produto[3])
        QuantidadeEntry.insert(0, produto[4])
        PrecoEntry.insert(0, produto[5])
        DataProdutoEntry.insert(0, produto[6])
    else:
        self.lblmsg["text"] = "Usuário não encontrado"
    LimparCampos()


buscarbotao = Button(text="BUSCAR", width=15,command=buscarUsuario)
buscarbotao.place (x=500 , y=90)


jan.mainloop()



 

