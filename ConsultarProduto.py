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

def GoToList():

        produto_list = Tk()
        produto_list.title("PRODUTOS - LISTA")
        produto_list.geometry("800x300")
        produto_list.configure(background="#f6f3ec")
        produto_list.resizable(width=False, height=False)

        colunas = ("Tipo", "Voltagem", "Marca", "Quantidade", "Preco", "Data")
        tree = ttk.Treeview(produto_list, columns=colunas, show="headings")

        tree.heading("ID", text="ID")
        tree.heading("Tipo", text="Tipo")
        tree.heading("Voltagem", text="Voltagem")
        tree.heading("Marca", text="Marca")
        tree.heading("Quantidade", text="Quantidade")
        tree.heading("Preco", text="Preço")
        tree.heading("Data", text="Data")


        tree.column("ID", width=50, anchor="center")
        tree.column("Tipo", width=100)
        tree.column("Voltagem", width=150)
        tree.column("Marca", width=120, anchor="center")
        tree.column("Quantidade", width=120)
        tree.column("Preco", width = 50)
        

        tree.pack(pady=10, padx=10, fill=BOTH, expand=False)

        VoltarButton = ttk.Button(produto_list, text = "Voltar", width = 8)
        VoltarButton.place(x = 10, y = 270)

def ListarProduto(self, idproduto):
    self.cursor.execute("SELECT * FROM produto WHERE idproduto = %s", (idproduto)) 
    return self.cursor.fetchone() 

Pergunta = Label (text="ID DO PRODUTO :", bg="#002333", fg="white")
Pergunta.place(x=70, y=100)
PerguntaEntry =ttk.Entry(width=30)
PerguntaEntry.place(x=190 , y=100)

buscarbotao = Button(text="BUSCAR", width=15,command=ListarProduto)
buscarbotao.place (x=190 , y=150)


jan.mainloop()
 

