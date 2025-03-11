from tkinter import * #Importa todos os mudulos do tkinter
from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
from tkinter import ttk
from DatabaseProduto import DataBase
import tkinter as tk


jan = Tk()
jan.title("USUARIO - PRODUTO")
jan.geometry("500x400")
jan.configure(background="#002333")
jan.resizable(width=False, height=False)

text_area = tk.Text(jan, height=10, width=40)
text_area.pack(pady=10)
text_area.place (x=70, y=200)

Pergunta = Label (text="TIPO DO PRODUTO :", bg="#002333", fg="white")
Pergunta.place(x=70, y=100)
PerguntaEntry =ttk.Entry(width=30)
PerguntaEntry.place(x=190 , y=100)

buscarbotao = Button(text="BUSCAR", width=15)
buscarbotao.place (x=190 , y=150)


jan.mainloop()
 

