from tkinter import *  # Importa todos os módulos do Tkinter
from tkinter import messagebox  # Importa o módulo de caixas de mensagens do Tkinter 
from tkinter import ttk  # Importa o módulo ttk do Tkinter
from DataBase import Database  # Importa a classe Database do módulo DataBase
import tkinter as tk  # Importa o módulo tkinter como tk

class Abrir_cliente:
    def __init__(self, root):

        tituloLabel = Label(text="CADASTRO DE CLIENTES", bg="#002333", fg="white", font=("Arial", 12, "bold"))
        tituloLabel.place(x=130, y=10)
        
        cpf_funcionarioLabel = Label(text="CPF:", bg="#002333", fg="white")
        cpf_funcionarioLabel.place(x=30, y=50)
        cpf_funcionarioEntry = ttk.Entry(width=40)
        cpf_funcionarioEntry.place(x=150, y=50)

        nome_funcionarioLabel = Label(text="Nome:", bg="#002333", fg="white")
        nome_funcionarioLabel.place(x=30, y=90)
        nome_funcionarioEntry = ttk.Entry(width=40)
        nome_funcionarioEntry.place(x=150, y=90)

        telefoneLabel = Label(text="Telefone:", bg="#002333", fg="white")
        telefoneLabel.place(x=30, y=130)
        telefoneEntry = ttk.Entry(width=40)
        telefoneEntry.place(x=150, y=130)

        emailLabel = Label(text="E-mail:", bg="#002333", fg="white")
        emailLabel.place(x=30, y=170)
        emailEntry = ttk.Entry(width=40)
        emailEntry.place(x=150, y=170)

