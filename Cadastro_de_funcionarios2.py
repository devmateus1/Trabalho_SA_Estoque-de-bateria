from tkinter import *  # Importa todos os módulos do Tkinter
from tkinter import messagebox  # Importa o módulo de caixas de mensagens do Tkinter 
from tkinter import ttk  # Importa o módulo ttk do Tkinter
#from DataBase import Database  # Importa a classe Database do módulo DataBase
import tkinter as tk  # Importa o módulo tkinter como tk

class Abrir_funcionario:
    def __init__(self, root):
        
        # Título da janela
        tituloLabel = Label(text="CADASTRO DE FUNCIONÁRIOS", bg="#002333", fg="white", font=("Arial", 12, "bold"))
        tituloLabel.place(x=130, y=10)

        # Labels e Campos de Entrada para os dados do funcionário
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

        data_da_contratacaoLabel = Label(text="Data de Contratação:", bg="#002333", fg="white")
        data_da_contratacaoLabel.place(x=30, y=210)
        data_da_contratacaoEntry = ttk.Entry(width=40)
        data_da_contratacaoEntry.place(x=150, y=210)

        cargoLabel = Label(text="Cargo:", bg="#002333", fg="white")
        cargoLabel.place(x=30, y=250)
        cargoEntry = ttk.Entry(width=40)
        cargoEntry.place(x=150, y=250)

        salarioLabel = Label(text="Salário:", bg="#002333", fg="white")
        salarioLabel.place(x=30, y=290)
        salarioEntry = ttk.Entry(width=40)
        salarioEntry.place(x=150, y=290)

        enderecoLabel = Label(text="Endereço:", bg="#002333", fg="white")
        enderecoLabel.place(x=30, y=330)
        enderecoEntry = ttk.Entry(width=40)
        enderecoEntry.place(x=150, y=330)

        # Função para conectar ao banco de dados e cadastrar funcionário
        def conect_banco_funcionario():
            cpf = cpf_funcionarioEntry.get()
            nome = nome_funcionarioEntry.get()
            telefone = telefoneEntry.get()
            email = emailEntry.get()
            dataDeContratacao = data_da_contratacaoEntry.get()
            cargo = cargoEntry.get()
            salario = salarioEntry.get()
            endereco = enderecoEntry.get()
            
            # Verifica se todos os campos estão preenchidos
            if cpf == "" or nome == "" or telefone == "" or email == "" or dataDeContratacao == "" or cargo == "" or salario == "" or endereco == "":
                messagebox.showerror(title="Erro de cadastro!", message="Todos os campos devem estar preenchidos!")
            else:
                db = Database()  # Cria uma instância do banco de dados
                db.RegistrarNoBancofuncionario(cpf, nome, telefone, email, dataDeContratacao, cargo, salario, endereco)  # Registra os dados
                messagebox.showinfo("Sucesso", "Funcionário(a) cadastrado(a) com sucesso!")
        
        # Botão de Cadastro
        CadastrarButton = ttk.Button(text="Cadastrar", width=15, command=conect_banco_funcionario)
        CadastrarButton.place(x=180, y=380)

        # Função para limpar os campos de entrada
        def LimparCampos():
            cpf_funcionarioEntry.delete(0, END)
            nome_funcionarioEntry.delete(0, END)
            telefoneEntry.delete(0, END)
            emailEntry.delete(0, END)
            data_da_contratacaoEntry.delete(0, END)
            cargoEntry.delete(0, END)
            salarioEntry.delete(0, END)
            enderecoEntry.delete(0, END)
        
        # Botão de Limpar Campos
        LimparButton = ttk.Button(text="Limpar", width=15, command=LimparCampos)
        LimparButton.place(x=290, y=380)
        

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    jan = Tk()  # Cria uma instância da janela principal
    jan.title("CADASTRO - Funcionários(a)")  # Define o título da janela
    jan.geometry("500x500")  # Define o tamanho da janela
    jan.configure(background="#002333")  # Configura a cor de fundo da janela
    jan.resizable(width=False, height=False)  # Impede que a janela seja redimensionada
    app = Abrir_funcionario(jan)  # Cria uma instância da classe Abrir_funcionario
    jan.mainloop()  # Inicia o loop principal da interface gráfica
