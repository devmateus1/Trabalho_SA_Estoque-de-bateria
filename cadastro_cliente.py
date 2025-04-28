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

        tituloLabel = Label(text="CADASTRO DE CLIENTE | ADM :",bg="#002333", fg="white") #Coloca um titulo para a janela
        tituloLabel.place(x=160,y=10)

        ClienteLabel = Label(text="Nome do Cliente:",bg="#002333", fg="white") #Cria label do fornecedor
        ClienteLabel.place(x=10,y=80)
        ClienteEntry=ttk.Entry(width=30) #Cria um campo do cliente
        ClienteEntry.place(x=150,y=80)   

        CpfClienteLabel = Label(text="CPF do Cliente:",bg="#002333", fg="white") #Cria label do Cpf
        CpfClienteLabel.place(x=10,y=120)
        CpfClienteEntry = ttk.Entry(width=30) #Cria um campo do cpf
        CpfClienteEntry.place(x=150,y=120)

        TelefoneClienteLabel = Label(text="Telefone do Cliente:",bg="#002333", fg="white") #Cria label do Telefone
        TelefoneClienteLabel.place(x=10,y=160)
        TelefoneClienteEntry = ttk.Entry(width=30) #Cria um campo do telefone
        TelefoneClienteEntry.place(x=150,y=160)

        EnderecoClienteLabel = Label(text="Endereço do Cliente:",bg="#002333", fg="white") #Cria label do endereço
        EnderecoClienteLabel.place(x=10,y=200)
        EnderecoClienteEntry = ttk.Entry(width=30) #Cria um campo do endereço
        EnderecoClienteEntry.place(x=150,y=200)

        def RegistrarNoBancoCliente(): #Registra os dados no banco de dados
            #Transforma os campos de textos em variaveis
            NomeCliente=ClienteEntry.get()
            cpf=CpfClienteEntry.get()
            telefone=TelefoneClienteEntry.get()
            endereco=EnderecoClienteEntry.get()



            if NomeCliente == "" or cpf == "" or telefone == "" or endereco == "" : #Verifica se os campos de textos estão vazios
                messagebox.showerror(title="Erro de Cadastro", message="PREENCHA TODOS OS CAMPOS") #Exibe a mensagem de erro
            else:
                db = Database() #Cria uma instancia da classe Database
                db.RegistrarNoBancoCliente(NomeCliente,cpf,telefone,endereco) #Chama o metodo para registrar no banco de dados 
                messagebox.showinfo("Sucesso","Fornecedor registrado com sucesso!") #Exibe a mensagem de sucesso
        CadastrarButton =  ttk.Button(text="Cadastrar",width=15,command=RegistrarNoBancoCliente) #Cria o botão de cadastro
        CadastrarButton.place(x=370,y=80)


        def LimparCampos():
            ClienteEntry.delete(0,END) #Limpa o campo de entrada do fornecedor
            CpfClienteEntry.delete(0,END) #Limpa o campo de entrada do cpf
            TelefoneClienteEntry.delete(0,END) #Limpa o campo de entrada do telefone
            EnderecoClienteEntry.delete(0,END) #Limpa o campo de entrada do endereço
           
        LimparButton =  ttk.Button(text="Limpar",width=15,command=LimparCampos) #Cria o botão de limpar
        LimparButton.place(x=500,y=80)
    
if __name__=="__main__":
    jan=Tk() # Cria uma instancia da janela principal
    jan.title("ADM - Fornecedores") #Define o titulo da janela
    jan .geometry("700x500") #Define o tamanho da janela
    jan.configure(bg="#002333") #Configura a cor de fundo da janela
    jan.resizable(width=False,height=False) #Impede que a janela seja redimensionad
    logo = PhotoImage(file="icon/_SLA_.png") # Carrega a imagem do logo
    LogoLabel = Label(image=logo, bg="#002333") # Cria um label para a imagem do logo
    LogoLabel.place(x=390, y=140) # Posiciona a imagem
    app = Abrir_Fornecedor(jan)
    jan.mainloop()