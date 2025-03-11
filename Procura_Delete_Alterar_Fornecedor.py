#Importar as biblotecas
from tkinter import * #IMporta todos os modulos do tkinter
from tkinter import messagebox #importa o modulo de caixas de de mensagens do tkinter 
from tkinter import ttk #Importa a classe Database do modulo DataBase
from DataBase import Database
import tkinter as tk

    #CRIAR A JANELA
jan=Tk() # Cria uma instancia da janela principal
jan.title("ADM - Leitor Fornecedor") #Define o titulo da janela
jan .geometry("700x700") #Define o tamanho da janela
jan.configure(background="white") #Configura a cor de fundo da janela
jan.resizable(width=False,height=False) #Impede que a janela seja redimensionad

tituloLabel = Label(text="FORNECEDORES:",bg="white") #Coloca um titulo para a janela
tituloLabel.place(x=160,y=10)

text_area = tk.Text(jan, height=10, width=40)
text_area.pack(pady=10)
text_area.place (x=200, y=200)
QuantidadeFornecedorEntry = ttk.Entry(width=30) #Cria um campo para colocar a quantidade de produto fornecido
QuantidadeFornecedorEntry.place(x=150,y=280)
id = QuantidadeFornecedorEntry.get()
def read_users(idfornecedor):
    db=Database
    db.buscar(idfornecedor)
    
    text_area.delete(1.0,ttk)
    
    text_area.insert(ttk,f"ID: {idfornecedor[1]}\n")
tk.Button(jan,text="Listar Usuario",command=read_users).grid(row=6,column=1,columnspan=1)
jan.mainloop()


