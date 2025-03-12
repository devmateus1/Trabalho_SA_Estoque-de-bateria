from tkinter import * #Importa todos os mudulos do tkinter
from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
from tkinter import ttk
from DataBase import Database
import tkinter as tk




jan = Tk()
jan.title("USUARIO - PRODUTO")
jan.geometry("500x400")
jan.configure(background="#002333")
jan.resizable(width=False, height=False)

colunas = ("Tipo", "Voltagem", "Marca", "Quantidade", "Preco", "Data")
tree = ttk.Treeview(jan, columns=colunas, show="headings")

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

jan.mainloop()