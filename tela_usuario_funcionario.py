from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from DataBase import Database
import tkinter as tk

class TelaGeral:
    def __init__(self, root):
        self.root = root  # Referência da janela principal

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

        # Botões
        button_bg = "#005577"  # Azul médio para botões
        button_fg = "white"

        # Botões existentes
        listarButton = ttk.Button(self.root, text="BUSCAR", width=15, command=self.buscarfuncionario)
        listarButton.place(x=200, y=420)
        
        listarButton = ttk.Button(self.root, text="limpar", width=15, command=self.LimparCampos)
        listarButton.place(x=310, y=420)

        # Botão "Voltar ao Menu" - Ajustando o uso do ttk.Button
        VoltarMenu = ttk.Button(self.root, text="Voltar ao menu", width=15, command=self.juntar_funcoes)
        VoltarMenu.place(x=90, y=420)  # Ajuste a posição conforme necessário

    # Funções para os botões (ainda precisam ser implementadas)
    
    def buscarfuncionario(self):
        idfuncionario = self.ID_funcionarioEntry.get()
        if idfuncionario == "":
            messagebox.showerror(title="Erro", message="PREENCHA O CAMPO DE ID")
        else:
            db = Database()  # Crie uma instância do banco de dados
            usuario = db.buscar_funcionario(idfuncionario)  # Supondo que exista um método para buscar por id
            if usuario:
                self.cpf_funcionarioEntry.delete(0, END)
                self.nome_funcionarioEntry.delete(0, END)
                self.telefoneEntry.delete(0, END)
                self.emailEntry.delete(0, END)
                self.data_da_contratacaoEntry.delete(0, END)
                self.cargoEntry.delete(0, END)
                self.salarioEntry.delete(0, END)
                self.enderecoEntry.delete(0, END)
                self.cpf_funcionarioEntry.insert(0, usuario[1])
                self.nome_funcionarioEntry.insert(0, usuario[2])
                self.telefoneEntry.insert(0, usuario[3])
                self.emailEntry.insert(0, usuario[4])
                self.data_da_contratacaoEntry.insert(0, usuario[5])
                self.cargoEntry.insert(0, usuario[6])
                self.salarioEntry.insert(0, usuario[7])
                self.enderecoEntry.insert(0, usuario[8])
            else:
                messagebox.showerror("Erro", "Funcionário não encontrado")
                self.LimparCampos()
    
    def LimparCampos(self):
            self.ID_funcionarioEntry.delete(0, END)
            self.cpf_funcionarioEntry.delete(0, END)
            self.nome_funcionarioEntry.delete(0, END)
            self.telefoneEntry.delete(0, END)
            self.emailEntry.delete(0, END)
            self.data_da_contratacaoEntry.delete(0, END)
            self.cargoEntry.delete(0, END)
            self.salarioEntry.delete(0, END)
            self.enderecoEntry.delete(0, END)
    
    def voltar_menu(self):
            self.root.destroy()  # Fecha a tela atual (tela de busca de produto)
            root = Tk()  # Cria uma nova instância da janela principal
            from tela_usuario import TeldACASTRO  # Importa a tela principal
            TeldACASTRO(root)  # Chama a tela principal

        # Função que junta as funcionalidades de voltar e limpar
    def juntar_funcoes(self):
        self.LimparCampos()
        self.voltar_menu()

if __name__ == "__main__":
    root = Tk()  # Cria uma instância da janela principal
    root.title("CADASTRO - Funcionários(a)")  # Define o título da janela
    root.geometry("500x500")  # Aumentei o tamanho da janela
    root.configure(background="#002333")  # Configura a cor de fundo da janela
    root.resizable(width=False, height=False)  # Impede que a janela seja redimensionada
    app = TelaGeral(root)  # Cria uma instância da classe TelaGeral
    root.mainloop()  # Inicia o loop principal da interface gráfica
 