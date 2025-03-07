from tkinter import * #Importa todos os mudulos do tkinter
from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
from tkinter import ttk
from DatabaseProduto import DataBase

jan = Tk()
jan.title("USUARIO - PRODUTO")
jan.geometry("800x400")
jan.configure(background="#002333")
jan.resizable(width=False, height=False)

Pergunta = Label (text="TIPO DO PRODUTO :", bg="#002333", fg="white")
Pergunta.place(x=100, y=100)
PerguntaEntry =ttk.Entry(width=30)
PerguntaEntry.place(x=220 , y=100)

buscarbotao = Button(text="BUSCAR", width=15)
buscarbotao.place (x=220 , y=150)
