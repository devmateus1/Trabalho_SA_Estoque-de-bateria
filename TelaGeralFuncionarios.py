from tkinter import *  # Importa todos os módulos do Tkinter
from tkinter import messagebox  # Importa o módulo de caixas de mensagens do Tkinter 
from tkinter import ttk  # Importa o módulo ttk do Tkinter
from DataBase import Database  # Importa a classe Database do módulo DataBase
import tkinter as tk  # Importa o módulo tkinter como tk

class TelaGeral:
    def __init__(self, root):
        self.root = root  # Referência da janela principal
        
        # Título da janela
        tituloLabel = Label(self.root, text="TELA GERAL FUNCIONÁRIOS", bg="#002333", fg="white", font=("Arial", 12, "bold"))
        tituloLabel.place(x=130, y=10)

        # Labels e Campos de Entrada para os dados do funcionário
        Label(self.root, text="ID DO FUNCIONARIO(A):", bg="#002333", fg="white").place(x=10, y=40)
        self.ID_funcionarioEntry = ttk.Entry(self.root, width=40)
        self.ID_funcionarioEntry.place(x=150, y=40)
         
        Label(self.root, text="CPF:", bg="#002333", fg="white").place(x=30, y=70)
        self.cpf_funcionarioEntry = ttk.Entry(self.root, width=40)
        self.cpf_funcionarioEntry.place(x=150, y=70)

        Label(self.root, text="Nome:", bg="#002333", fg="white").place(x=30, y=110)
        self.nome_funcionarioEntry = ttk.Entry(self.root, width=40)
        self.nome_funcionarioEntry.place(x=150, y=110)

        Label(self.root, text="Telefone:", bg="#002333", fg="white").place(x=30, y=150)
        self.telefoneEntry = ttk.Entry(self.root, width=40)
        self.telefoneEntry.place(x=150, y=150)

        Label(self.root, text="E-mail:", bg="#002333", fg="white").place(x=30, y=190)
        self.emailEntry = ttk.Entry(self.root, width=40)
        self.emailEntry.place(x=150, y=190)

        Label(self.root, text="Data de Contratação:", bg="#002333", fg="white").place(x=30, y=230)
        self.data_da_contratacaoEntry = ttk.Entry(self.root, width=40)
        self.data_da_contratacaoEntry.place(x=150, y=230)

        Label(self.root, text="Cargo:", bg="#002333", fg="white").place(x=30, y=270)
        self.cargoEntry = ttk.Entry(self.root, width=40)
        self.cargoEntry.place(x=150, y=270)

        Label(self.root, text="Salário:", bg="#002333", fg="white").place(x=30, y=310)
        self.salarioEntry = ttk.Entry(self.root, width=40)
        self.salarioEntry.place(x=150, y=310)

        Label(self.root, text="Endereço:", bg="#002333", fg="white").place(x=30, y=350)
        self.enderecoEntry = ttk.Entry(self.root, width=40)
        self.enderecoEntry.place(x=150, y=350)

        # Botões
        excluirButton = ttk.Button(self.root, text="EXCLUIR", width=15, command=self.excluir_funcionario)
        excluirButton.place(x=50, y=400)

        alterarButton = ttk.Button(self.root, text="ALTERAR", width=15, command=self.alterar_funcionario)
        alterarButton.place(x=200, y=400)

        listarButton = ttk.Button(self.root, text="buscar", width=15, command=self.buscarfuncionario)
        listarButton.place(x=350, y=400)

    # Funções para os botões (ainda precisam ser implementadas)
    def excluir_funcionario(self):
        print("Excluir funcionário")

    def alterar_funcionario(self):
        print("Alterar funcionário")

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
        


if __name__ == "__main__":
    jan = Tk()  # Cria uma instância da janela principal
    jan.title("CADASTRO - Funcionários(a)")  # Define o título da janela
    jan.geometry("500x500")  # Define o tamanho da janela
    jan.configure(background="#002333")  # Configura a cor de fundo da janela
    jan.resizable(width=False, height=False)  # Impede que a janela seja redimensionada
    app = TelaGeral(jan)  # Cria uma instância da classe TelaGeral
    jan.mainloop()  # Inicia o loop principal da interface gráfica
