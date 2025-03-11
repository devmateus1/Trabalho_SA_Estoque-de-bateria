import tkinter as tk
from tkinter import messagebox
from tkinter.constants import END
from DataBaseFornecedor import Database


class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastrar usuário(a)")
        self.root.geometry('500x450')
        self.root.configure(bg="#002333") 

        # Criação de WIDGETS
        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self.root, text="id_func: ", font=("Arial", 14), fg="white", bg="#002333").place(x=20, y=30)
        tk.Label(self.root, text="nome: ", font=("Arial", 14), fg="white", bg="#002333").place(x=20, y=70)
        tk.Label(self.root, text="telefone: ", font=("Arial", 14), fg="white", bg="#002333").place(x=20, y=110)
        tk.Label(self.root, text="email: ", font=("Arial", 14), fg="white", bg="#002333").place(x=20, y=150)
        tk.Label(self.root, text="cargo: ", font=("Arial", 14), fg="white", bg="#002333").place(x=20, y=190)
        tk.Label(self.root, text="salário: ", font=("Arial", 14), fg="white", bg="#002333").place(x=20, y=230)
        tk.Label(self.root, text="cidade: ", font=("Arial", 14), fg="white", bg="#002333").place(x=20, y=270)
        tk.Label(self.root, text="bairro: ", font=("Arial", 14), fg="white", bg="#002333").place(x=20, y=310)

        self.id_func_entry = tk.Entry(self.root, width=35)
        self.nome_entry = tk.Entry(self.root, width=35)
        self.telefone_entry = tk.Entry(self.root, width=35)
        self.email_entry = tk.Entry(self.root, width=35)
        self.cargo_entry = tk.Entry(self.root, width=35)
        self.salario_entry = tk.Entry(self.root, width=35)
        self.cidade_entry = tk.Entry(self.root, width=35)
        self.bairro_entry = tk.Entry(self.root, width=35)

        self.id_func_entry.place(x=120, y=35)
        self.nome_entry.place(x=120, y=75)
        self.telefone_entry.place(x=120, y=115)
        self.email_entry.place(x=120, y=155)
        self.cargo_entry.place(x=120, y=195)
        self.salario_entry.place(x=120, y=235)
        self.cidade_entry.place(x=120, y=275)
        self.bairro_entry.place(x=120, y=315)

        # Botões
        tk.Button(self.root, text="Cadastrar", command=self.RegistrarNoBancoFuncionario, font=("Arial", 12)).place(x=80, y=370, width=160, height=35)
        tk.Button(self.root, text="Limpar", command=self.limpar_campos, font=("Arial", 12)).place(x=80, y=400, width=160, height=35)
        

    def RegistrarNoBancoFuncionario(self): #Registra os dados no banco de dados
            #Transforma os campos de textos em variaveis
            id_func=self.id_func_entry.get()
            nome=self.nome_entry.get()
            telefone= self.telefone_entry.get()
            email= self.email_entry.get()
            cargo=self.cargo_entry.get()
            salario=self.salario_entry.get()
            cidade=self.cidade_entry.get()
            bairro=self.bairro_entry.get()


            if id_func == "" or nome == "" or telefone == "" or email == "" or cargo == "" or salario == "" or cidade == "" or bairro == "" : #Verifica se os campos de textos estão vazios
                messagebox.showerror(title="Erro de Cadastro", message="PREENCHA TODOS OS CAMPOS") #Exibe a mensagem de erro
            else:
                db = Database() #Cria uma instancia da classe Database
                db.RegistrarNoBanco(id_func,nome,telefone,email, cargo,salario, cidade,bairro) #Chama o metodo para registrar no banco de dados 
                messagebox.showinfo("Sucesso","Funcionario registrado com sucesso!") #Exibe a mensagem de sucesso
       
    

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



