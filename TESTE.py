from tkinter import *
from tkinter import ttk

def exibir_selecao():
    # Exibe a opção selecionada pelo usuário
    selecionado = combo_box.get()
    label_resultado.config(text=f"Você selecionou: {selecionado}")

# Configura a janela principal
root = Tk()
root.title("Exemplo de ComboBox")
root.geometry("300x200")

# Lista de opções para o ComboBox
opcoes = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]

# Cria o ComboBox e coloca na interface
combo_box = ttk.Combobox(root, values=opcoes, state="readonly")  # 'readonly' para não permitir digitar
combo_box.place(x=50, y=50)

# Cria um botão para exibir a seleção do ComboBox
botao = Button(root, text="Exibir Seleção", command=exibir_selecao)
botao.place(x=50, y=100)

# Rótulo para exibir a seleção do ComboBox
label_resultado = Label(root, text="")
label_resultado.place(x=50, y=150)

# Inicia o loop da interface gráfica
root.mainloop()
