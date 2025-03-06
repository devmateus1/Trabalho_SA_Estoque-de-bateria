from tkinter import * #Importa todos os mudulos do tkinter
from tkinter import messagebox # Importar o mudulo de widgets tematicos do tkinter
from tkinter import ttk
#from DataBase import DataBase

# Criar a janela
jan = Tk()
jan.title("Tela de adm - Painel de Acesso")
jan.geometry("600x300")
jan.configure(background="#002333")
jan.resizable(width=False, height=False)



Produtolabel = Label (text="PRODUTO:", bg="#002333" , fg="white")
Produtolabel.place (x=160 , y=70)
ProdutoEntry = ttk.Entry (width=15)
ProdutoEntry.place (x=250 ,y=70)

Fornecedorlabel = Label (text="FORNECEDOR:", bg="#002333" , fg="white")
Fornecedorlabel.place (x=160 , y=100)
FornecedorEntry = ttk.Entry (width=15)
FornecedorEntry.place (x=250 ,y=100)


Funcionariolabel = Label (text="FUNCIONARIO:", bg="#002333" , fg="white")
Funcionariolabel.place (x=160 , y=130)
FuncionarioEntry = ttk.Entry (width=15)
FuncionarioEntry.place (x=250 ,y=130)


jan.mainloop()