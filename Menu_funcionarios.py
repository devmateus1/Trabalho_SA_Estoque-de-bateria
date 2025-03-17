import tkinter as tk
from tkinter import Menu

# Funções para abrir diferentes janelas
def abrir_janela1():
    janela1 = tk.Toplevel(root)
    janela1.title("Janela 1")
    tk.Label(janela1, text="Você abriu a Janela 1!").pack(pady=20)

def abrir_janela2():
    janela2 = tk.Toplevel(root)
    janela2.title("Janela 2")
    tk.Label(janela2, text="Você abriu a Janela 2!").pack(pady=20)

# Criando a janela principal
root = tk.Tk()
root.title("Sistema com Menu")
root.geometry("400x300")

# Criando a barra de menu
menu_bar = Menu(root)

# Criando um menu "Opções"
menu_opcoes = Menu(menu_bar, tearoff=0)
menu_opcoes.add_command(label="Abrir Janela 1", command=abrir_janela1)
menu_opcoes.add_command(label="Abrir Janela 2", command=abrir_janela2)
menu_opcoes.add_separator()
menu_opcoes.add_command(label="Sair", command=root.quit)

# Adicionando o menu à barra de menu
menu_bar.add_cascade(label="Opções", menu=menu_opcoes)

# Configurando a janela para usar essa barra de menu
root.config(menu=menu_bar)

# Rodando o sistema
root.mainloop()
