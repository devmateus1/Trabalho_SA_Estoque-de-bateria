from tkinter import *  # Importa todos os módulos do Tkinter
from tkinter import messagebox  # Importa o módulo de caixas de mensagens do Tkinter 
from tkinter import ttk  # Importa o módulo ttk do Tkinter
from DataBase import Database  # Importa a classe Database do módulo DataBase
import tkinter as tk  # Importa o módulo tkinter como tk

class TelaGeral:
    def __init__(self, root):
        self.root = root  
        self.root.configure(bg="#002333")  # Fundo da janela principal
        
        # Título da janela
        tituloLabel = Label(self.root, text="TELA GERAL FUNCIONÁRIOS", bg="#002333", fg="white", font=("Arial", 13, "bold"))
        tituloLabel.place(x=140, y=10)

        # Labels e Campos de Entrada para os dados do funcionário
        field_bg = "#004455"  # Azul escuro para os campos
        text_fg = "white"  # Cor do texto

        Label(self.root, text="ID DO FUNCIONARIO(A):", bg="#002333", fg=text_fg).place(x=30, y=50)
        self.ID_funcionarioEntry = ttk.Entry(self.root, width=40)
        self.ID_funcionarioEntry.place(x=200, y=50)
         
        Label(self.root, text="CPF:", bg="#002333", fg=text_fg).place(x=30, y=90)
        self.cpf_funcionarioEntry = ttk.Entry(self.root, width=40)
        self.cpf_funcionarioEntry.place(x=200, y=90)

        Label(self.root, text="Nome:", bg="#002333", fg=text_fg).place(x=30, y=130)
        self.nome_funcionarioEntry = ttk.Entry(self.root, width=40)
        self.nome_funcionarioEntry.place(x=200, y=130)

        Label(self.root, text="Telefone:", bg="#002333", fg=text_fg).place(x=30, y=170)
        self.telefoneEntry = ttk.Entry(self.root, width=40)
        self.telefoneEntry.place(x=200, y=170)

        Label(self.root, text="E-mail:", bg="#002333", fg=text_fg).place(x=30, y=210)
        self.emailEntry = ttk.Entry(self.root, width=40)
        self.emailEntry.place(x=200, y=210)

        Label(self.root, text="Data de Contratação:", bg="#002333", fg=text_fg).place(x=30, y=250)
        self.data_da_contratacaoEntry = ttk.Entry(self.root, width=40)
        self.data_da_contratacaoEntry.place(x=200, y=250)

        Label(self.root, text="Cargo:", bg="#002333", fg=text_fg).place(x=30, y=290)
        self.cargoEntry = ttk.Entry(self.root, width=40)
        self.cargoEntry.place(x=200, y=290)

        Label(self.root, text="Salário:", bg="#002333", fg=text_fg).place(x=30, y=330)
        self.salarioEntry = ttk.Entry(self.root, width=40)
        self.salarioEntry.place(x=200, y=330)

        Label(self.root, text="Endereço:", bg="#002333", fg=text_fg).place(x=30, y=370)
        self.enderecoEntry = ttk.Entry(self.root, width=40)
        self.enderecoEntry.place(x=200, y=370)

        # Botões (reorganizados e estilizados)
        button_bg = "#005577"  # Azul médio para botões
        button_fg = "white"

        excluirButton = ttk.Button(self.root, text="EXCLUIR", width=15, command=self.combinarfuncoes)
        excluirButton.place(x=60, y=420)

        alterarButton = ttk.Button(self.root, text="ALTERAR", width=15, command=self.alterarfuncionario)
        alterarButton.place(x=200, y=420)

        listarButton = ttk.Button(self.root, text="BUSCAR", width=15, command=self.buscarfuncionario)
        listarButton.place(x=340, y=420)

    # Funções para os botões (ainda precisam ser implementadas)
    def excluirFuncionario(self):
            idfuncionario=self.ID_funcionarioEntry.get()
            if idfuncionario =="":
                messagebox.showerror(title="Erro de Busca", message="PREENCHA O CAMPO DE ID") #Exibe a mensagem de erro
            else:
                db = Database()
                db.removerfuncionario(idfuncionario)
                messagebox.showinfo("Sucesso","funcionario excluido com sucesso com sucesso!") #Exibe a mensagem de sucesso
    def buscar_funcionario(self):
        id_funcionario = self.id_entry.get()

        if not id_funcionario:
            messagebox.showerror("Erro", "Digite um ID para buscar")
            return

        funcionario = self.db.buscar_funcionario(id_funcionario)

        if funcionario:

            self.cpf_funcionarioEntry.delete(0, tk.END)
            self.cpf_funcionarioEntry.insert(0, funcionario[1])  # CPF
            
            self.nome_funcionarioEntry.delete(0, tk.END)
            self.nome_funcionarioEntry.insert(0, funcionario[2])  # Nome

            self.telefoneEntry.delete(0, tk.END)
            self.telefoneEntry.insert(0, funcionario[3])

            self.emailEntry.delete(0, tk.END)
            self.emailEntry.insert(0, funcionario[4])

            self.data_da_contratacaoEntry.delete(0, tk.END)
            self.data_da_contratacaoEntry.insert(0, funcionario[5])

            self.cargoEntry.delete(0, tk.END)
            self.cargoEntry.insert(0, funcionario[6])  # Cargo

            self.salarioEntry.delete(0, tk.END)
            self.salarioEntry.insert(0, funcionario[7])  # Salário

            self.enderecoEntry.delete(0, tk.END)
            self.enderecoEntry.insert(0, funcionario[8])  # Salário

        else:
            messagebox.showerror("Erro", "Funcionário não encontrado")


    def alterarfuncionario(self):
            idfuncionario = self.ID_funcionarioEntry.get()
            cpf = self.cpf_funcionarioEntry.get()
            nome = self.nome_funcionarioEntry.get()
            telefone = self.telefoneEntry.get()
            email = self.emailEntry.get()
            dataDeContratacao = self.data_da_contratacaoEntry.get()
            cargo = self.cargoEntry.get()
            salario = self.salarioEntry.get()
            endereco = self.enderecoEntry.get()
            
            # Verifica se todos os campos estão preenchidos
            if  idfuncionario == "" or cpf == "" or nome == "" or telefone == "" or email == "" or dataDeContratacao == "" or cargo == "" or salario == "" or endereco == "":
                messagebox.showerror(title="Erro!", message="Todos os campos devem estar preenchidos!")
            else:
                db = Database()  # Cria uma instância do banco de dados
                db.alterarfuncionario(idfuncionario, cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco)  # Registra os dados
                messagebox.showinfo("Sucesso", "Funcionário(a) cadastrado(a) com sucesso!")
        

    

    def buscarfuncionario(self):
        ID_funcionarioEntry = self.ID_funcionarioEntry.get()
        self.cursor.execute("SELECT * FROM funcionario WHERE ID_funcionarioEntry=%s", (ID_funcionarioEntry,))
        usuario = self.cursor.fetchone()
        if usuario:
            self.cpf_funcionarioEntry.insert(0, usuario[1])
            self.nome_funcionarioEntry.insert(0, usuario[2])
            self.telefoneEntry.insert(0, usuario[3])
            self.emailEntry.insert(0, usuario[4])
            self.data_da_contratacaoEntry.insert(0, usuario[5])
            self.cargoEntry.insert(0, usuario[6])
            self.salarioEntry.insert(0, usuario[7])
            self.enderecoEntry.insert(0, usuario[8])
        else:
            self.lblmsg["text"] = "Funcionario não encontrado"
            self.limparCampos()
    
    def LimparCampos(self):
            self.cpf_funcionarioEntry.delete(0, END)
            self.nome_funcionarioEntry.delete(0, END)
            self.telefoneEntry.delete(0, END)
            self.emailEntry.delete(0, END)
            self.data_da_contratacaoEntry.delete(0, END)
            self.cargoEntry.delete(0, END)
            self.salarioEntry.delete(0, END)
            self.enderecoEntry.delete(0, END)
    
    def combinarfuncoes(self):
         self.excluirFuncionario()
         self.LimparCampos()


if __name__ == "__main__":
    jan = Tk()  # Cria uma instância da janela principal
    jan.title("CADASTRO - Funcionários(a)")  # Define o título da janela
    jan.geometry("500x500")  # Define o tamanho da janela
    jan.configure(background="#002333")  # Configura a cor de fundo da janela
    jan.resizable(width=False, height=False)  # Impede que a janela seja redimensionada
    app = TelaGeral(jan)  # Cria uma instância da classe TelaGeral
    jan.mainloop()  # Inicia o loop principal da interface gráfica
