'''import tkinter as tk
from tkinter import messagebox
from tkinter.constants import END
import mysql.connector

# Conectar ao banco de dados MySQL
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Substitua pelo seu usuário do MySQL
        password="",  # Substitua pela sua senha do MySQL
        database="trabalho_sa"
    )

# Criar a tabela se não existir
def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id_func INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            telefone VARCHAR(20),
            email VARCHAR(100),
            cargo VARCHAR(50),
            salario DECIMAL(10,2),
            cidade VARCHAR(50),
            bairro VARCHAR(50)
        )
    """)
    conexao.commit()
    conexao.close()

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastrar usuário(a)")
        self.root.geometry('500x450')
        self.root.configure(bg="#002333")

        # Criar tabela no banco de dados
        criar_tabela()

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
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        cargo = self.cargo_entry.get()
        salario = self.salario_entry.get()
        cidade = self.cidade_entry.get()
        bairro = self.bairro_entry.get()

        if not nome or not telefone or not email or not cargo or not salario or not cidade or not bairro:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        try:
            conexao = conectar_banco()
            cursor = conexao.cursor()
            cursor.execute("""
                INSERT INTO funcionarios (nome, telefone, email, cargo, salario, cidade, bairro) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (nome, telefone, email, cargo, salario, cidade, bairro))
            conexao.commit()
            conexao.close()

            messagebox.showinfo("Info", "Usuário cadastrado com sucesso!")
            self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

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
root.mainloop()'''
