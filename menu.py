"""from tkinter import *  # Importa todos os módulos do Tkinter
from tkinter import messagebox  # Importa o módulo de caixas de mensagens do Tkinter 
from tkinter import ttk  # Importa o módulo ttk do Tkinter
import tkinter as tk  # Importa o módulo tkinter como tk

class abrir_Menu:
    def __init__(self, root):
        # CadastrarButton = ttk.Button(jan, text="Cadastrar", width=15, command=conect_banco_funcionario)
        funcionario= ttk.Button(jan, text="funcionario",whidt=15,)"""

import tkinter as tk
from tkinter import messagebox

# Funções que serão chamadas quando os itens do menu forem selecionados
def novo_arquivo():
    messagebox.showinfo("Novo Arquivo", "Você selecionou 'Novo Arquivo'")


def abrir_arquivo():
    messagebox.showinfo("Abrir Arquivo", "Você selecionou 'Abrir Arquivo'")


def salvar_arquivo():
    messagebox.showinfo("Salvar Arquivo", "Você selecionou 'Salvar Arquivo'")


def sobre():
    messagebox.showinfo("Sobre", "Este é um Menu em Tkinter")
    

# Cria a janela principal
root = tk.Tk()
root.title("Menu")

# Cria uma barra de menu
menu_bar = tk.Menu(root)

# Cria um menu "Arquivo" e adiciona itens
menu_arquivo = tk.Menu(menu_bar, tearoff=0)
menu_arquivo.add_command(label="Novo", command=novo_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=root.quit)
menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)

# Cria um menu "Ajuda" e adiciona itens
menu_ajuda = tk.Menu(menu_bar, tearoff=0)
menu_ajuda.add_command(label="Sobre", command=sobre)
menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

# Configura a barra de menu na janela principal
root.config(menu=menu_bar)

# Inicia o loop principal da interface gráfica
root.mainloop()