#Importar as biblotecas
from tkinter import * #IMporta todos os modulos do tkinter
from tkinter import messagebox #importa o modulo de caixas de de mensagens do tkinter 
from tkinter import ttk #Importa a classe Database do modulo DataBase
from DataBase import Database
import tkinter as tk

class Abrir_Fornecedor:
    def __init__(self,root):
       

        

        #CRIAR A JANELA
        
        #CRIA OS LABELS NECESSARIOS

        tituloLabel = Label(text="CADASTRO DE FORNECEDORES:",bg="white") #Coloca um titulo para a janela
        tituloLabel.place(x=160,y=10)

        FornecedorLabel = Label(text="Nome do Fornecedor:",bg="White") #Cria label do fornecedor
        FornecedorLabel.place(x=10,y=40)
        FornecedorEntry=ttk.Entry(width=30) #Cria um campo do forncedor
        FornecedorEntry.place(x=150,y=40)   

        CpfFornecedorLabel = Label(text="CPF do Fornecedor:",bg="White") #Cria label do Cpf
        CpfFornecedorLabel.place(x=10,y=80)
        CpfFornecedorEntry = ttk.Entry(width=30) #Cria um campo do cpf
        CpfFornecedorEntry.place(x=150,y=80)

        TelefoneFornecedorLabel = Label(text="Telefone do fornecedor:",bg="White") #Cria label do Telefone
        TelefoneFornecedorLabel.place(x=10,y=120)
        TelefoneFornecedorEntry = ttk.Entry(width=30) #Cria um campo do telefone
        TelefoneFornecedorEntry.place(x=150,y=120)

        EmailFornecedorLabel = Label(text="Email do Fornecedor:",bg="White") #Cria label do email
        EmailFornecedorLabel.place(x=10,y=160)
        EmailFornecedorEntry = ttk.Entry(width=30) #Cria um campo do email
        EmailFornecedorEntry.place(x=150,y=160)

        EnderecoFornecedorLabel = Label(text="Endereço do Fornecedor:",bg="White") #Cria label do endereço
        EnderecoFornecedorLabel.place(x=10,y=200)
        EnderecoFornecedorEntry = ttk.Entry(width=30) #Cria um campo do endereço
        EnderecoFornecedorEntry.place(x=150,y=200)

        ProdutoFornecedorLabel = Label(text="Produto Fornecido:",bg="White") #Cria label do produto
        ProdutoFornecedorLabel.place(x=10,y=240)
        ProdutoFornecedorEntry = ttk.Entry(width=30) #Cria um campo do produto
        ProdutoFornecedorEntry.place(x=150,y=240)

        QuantidadeFornecedorLabel = Label(text="Quantia de Produto:",bg="White") #Cria label da quantidade de produto fornecido 
        QuantidadeFornecedorLabel.place(x=10,y=280)
        QuantidadeFornecedorEntry = ttk.Entry(width=30) #Cria um campo para colocar a quantidade de produto fornecido
        QuantidadeFornecedorEntry.place(x=150,y=280)

        def RegistrarNoBancoFornecedor(): #Registra os dados no banco de dados
            #Transforma os campos de textos em variaveis
            fornecedores=FornecedorEntry.get()
            cpf=CpfFornecedorEntry.get()
            telefone=TelefoneFornecedorEntry.get()
            email=EmailFornecedorEntry.get()
            endereco=EnderecoFornecedorEntry.get()
            produto=ProdutoFornecedorEntry.get()
            quantidade=QuantidadeFornecedorEntry.get()


            if fornecedores == "" or cpf == "" or telefone == "" or email == "" or endereco == "" or produto == "" or quantidade == "": #Verifica se os campos de textos estão vazios
                messagebox.showerror(title="Erro de Cadastro", message="PREENCHA TODOS OS CAMPOS") #Exibe a mensagem de erro
            else:
                db = Database() #Cria uma instancia da classe Database
                db.RegistrarNoBanco(fornecedores,cpf,telefone,email,endereco,produto,quantidade) #Chama o metodo para registrar no banco de dados 
                messagebox.showinfo("Sucesso","Fornecedor registrado com sucesso!") #Exibe a mensagem de sucesso
        CadastrarButton =  ttk.Button(text="Cadastrar",width=15,command=RegistrarNoBancoFornecedor) #Cria o botão de cadastro
        CadastrarButton.place(x=70,y=350)


        def LimparCampos():
            FornecedorEntry.delete(0,END) #Limpa o campo de entrada do fornecedor
            CpfFornecedorEntry.delete(0,END) #Limpa o campo de entrada do cpf
            TelefoneFornecedorEntry.delete(0,END) #Limpa o campo de entrada do telefone
            EmailFornecedorEntry.delete(0,END) #Limpa o campo de entrada do email
            EnderecoFornecedorEntry.delete(0,END) #Limpa o campo de entrada do endereço
            ProdutoFornecedorEntry.delete(0,END) #Limpa o campo de entrada do produto
            QuantidadeFornecedorEntry.delete(0,END) #Limpa o campo de entrada da quantidade de produto


        LimparButton =  ttk.Button(text="Limpar",width=15,command=LimparCampos) #Cria o botão de limpar
        LimparButton.place(x=280,y=350)
    
if __name__=="__main__":
    jan=Tk() # Cria uma instancia da janela principal
    jan.title("ADM - Fornecedores") #Define o titulo da janela
    jan .geometry("500x500") #Define o tamanho da janela
    jan.configure(background="white") #Configura a cor de fundo da janela
    jan.resizable(width=False,height=False) #Impede que a janela seja redimensionad
    app = Abrir_Fornecedor(jan)
    jan.mainloop()