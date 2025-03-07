from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Criar a janela principal
jan = Tk()
jan.title("Sistema - Painel de Acesso")
jan.geometry("400x300")
jan.configure(background="#002333")
jan.resizable(width=False, height=False)

# Função para verificar login
def verificar_login():
    usuario = loginEntry.get()
    senha = senhaEntry.get()

# Verificação de credenciais
    if usuario == "adm" and senha == "adm123":
        abrir_tela_adm()
    elif usuario == "usuario" and senha == "user123":
        abrir_tela_usuario()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Função para abrir a tela do administrador
def abrir_tela_adm():
    messagebox.showinfo("Sucesso", "Login como Administrador!")
jan.destroy() # Fecha a tela de login
tela_adm = Tk()
tela_adm.title("Tela do Administrador")
tela_adm.geometry("400x300")

# Aqui você pode adicionar widgets para edição
Label(tela_adm, text="Bem-vindo, Administrador!", font=("Arial", 16)).pack(pady=20)

# Exemplo de botão para editar dados
def editar_dados():
    messagebox.showinfo("Editar Dados", "Aqui você pode editar os dados.")

editar_button = Button(tela_adm, text="Editar Dados", command=editar_dados)
editar_button.pack(pady=10)

# Iniciar a aplicação do ADM
tela_adm.mainloop()

# Função para abrir a tela do usuário
def abrir_tela_usuario():
    messagebox.showinfo("Sucesso", "Login como Usuário!")
jan.destroy() # Fecha a tela de login
tela_usuario = Tk()
tela_usuario.title("Tela do Usuário")
tela_usuario.geometry("400x300")

Label(tela_usuario, text="Bem-vindo, Usuário!", font=("Arial", 16)).pack(pady=20)

# Aqui você pode adicionar widgets para visualizar dados
Label(tela_usuario, text="Aqui estão os dados disponíveis:").pack(pady=10)

# Exemplo de visualização de dados
dados = "ola"

for dado in dados:
    Label(tela_usuario, text=dado).pack()

# Iniciar a aplicação do Usuário
tela_usuario.mainloop()

# Labels e Entradas na tela de login
loginLabel = Label(jan, text="LOGIN", bg="#002333", fg="white")
loginLabel.place(x=150, y=50)
loginEntry = ttk.Entry(jan, width=20)
loginEntry.place(x=150, y=80)

senhaLabel = Label(jan, text="SENHA", bg="#002333", fg="white")
senhaLabel.place(x=150, y=110)
senhaEntry = ttk.Entry(jan, width=20, show='*')
senhaEntry.place(x=150, y=140)

# Botão de Login
loginButton = ttk.Button(jan, text="Login", command=verificar_login)
loginButton.place(x=170, y=180)

# Iniciar a aplicação inicial
jan.mainloop()