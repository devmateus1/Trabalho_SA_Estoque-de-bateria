import tkinter as tk
from tkinter import messagebox
from tkinter.constants import END
#from crud import create_user, read_users, update_user, delete_user

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastrar usuário(a)")
        self.root.geometry('800x400')
        self.root.configure(bg="#002333") 

        # Criação de WIDGETS
        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="id_func: ", font=("Arial", 12), fg="white", bg="#002333").place(x=10, y=20)
        tk.Label(self.root, text="nome: ", font=("Arial", 12), fg="white", bg="#002333").place(x=10, y=55)
        tk.Label(self.root, text="telefone: ", font=("Arial", 12), fg="white", bg="#002333").place(x=10, y=85)
        tk.Label(self.root, text="email: ", font=("Arial", 12), fg="white", bg="#002333").place(x=10, y=115)
        tk.Label(self.root, text="cargo: ", font=("Arial", 12), fg="white", bg="#002333").place(x=10, y=145)
        tk.Label(self.root, text="salário: ", font=("Arial", 12), fg="white", bg="#002333").place(x=10, y=175)
        tk.Label(self.root, text="cidade: ", font=("Arial", 12), fg="white", bg="#002333").place(x=10, y=205)
        tk.Label(self.root, text="bairro: ", font=("Arial", 12), fg="white", bg="#002333").place(x=10, y=235)

        self.id_func_entry = tk.Entry(self.root)
        self.nome_entry = tk.Entry(self.root)
        self.telefone_entry = tk.Entry(self.root)
        self.email_entry = tk.Entry(self.root)
        self.cargo_entry = tk.Entry(self.root)
        self.salario_entry = tk.Entry(self.root)
        self.cidade_entry = tk.Entry(self.root)
        self.bairro_entry = tk.Entry(self.root)

        self.id_func_entry.place(x=80, y=25)
        self.nome_entry.place(x=80, y=55)
        self.telefone_entry.place(x=80, y=85)
        self.email_entry.place(x=80, y=115)
        self.cargo_entry.place(x=80, y=145)
        self.salario_entry.place(x=80, y=175)
        self.cidade_entry.place(x=80, y=205)
        self.bairro_entry.place(x=80, y=235)

        # Botões
        tk.Button(self.root, text="Cadastrar", command=self.create_user).place(x=53, y=270, width=150, height=30)
        tk.Button(self.root, text="Limpar", command=self.limpar_campos).place(x=210, y=270, width=150, height=30)

    def create_user(self):
        # Placeholder para a funcionalidade de criação de usuário
        messagebox.showinfo("Info", "Usuário cadastrado com sucesso!")

    def limpar_campos(self):
        self.id_func_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.cargo_entry.delete(0, END)
        self.salario_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.bairro_entry.delete(0, END)

root = tk.Tk()
app = CRUDApp(root)
root.mainloop()