#Importar as biblotecas
from tkinter import * #IMporta todos os modulos do tkinter
from tkinter import messagebox #importa o modulo de caixas de de mensagens do tkinter 
from tkinter import ttk #Importa a classe Database do modulo DataBase
from DataBaseFornecedor import Database
import tkinter as tk

    #CRIAR A JANELA
jan=Tk() # Cria uma instancia da janela principal
jan.title("ADM - Leitor Fornecedor") #Define o titulo da janela
jan .geometry("700x700") #Define o tamanho da janela
jan.configure(background="white") #Configura a cor de fundo da janela
jan.resizable(width=False,height=False) #Impede que a janela seja redimensionad

tituloLabel = Label(text="FORNECEDORES:",bg="white") #Coloca um titulo para a janela
tituloLabel.place(x=160,y=10)
def create_widgets(self):
    self.text_area = tk.Text(self,height=10,width=80)
    self.text_area.grid(row=10,column=0,columnspan=4)


def read_users(self):
    users =read_users()
    self.text_area.delete(1.0,ttk.END)
    for user in users:
        self.text_area.insert(ttk.END,f"ID: {user[0]}, Nome: {user[1]}, Telefone: {user[2]}, Email: {user[3]}\n")

jan.mainloop()


