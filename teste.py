import tkinter as tk
from tkinter import ttk

# Lista de fornecedores
fornecedores = ["Fornecedor A", "Fornecedor B", "Fornecedor C"]

# Criar a janela principal
janela = tk.Tk()
janela.title("Seleção de Fornecedor")
janela.geometry("300x150")

# Rótulo
label = tk.Label(janela, text="Selecione o fornecedor:")
label.pack(pady=10)

# Criar o ComboBox
combo = ttk.Combobox(janela, values=fornecedores, state="readonly")
combo.place(x=10, y=10)

# Função para capturar a seleção
def selecionar_fornecedor(event):
    fornecedor_selecionado = combo.get()
    print("Fornecedor selecionado:", fornecedor_selecionado)

# Associar a função ao evento de seleção
combo.bind("<<ComboboxSelected>>", selecionar_fornecedor)

# Iniciar a interface
janela.mainloop()
