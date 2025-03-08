import tkinter as tk

# Criar a janela principal
janela = tk.Tk()
janela.title("Exemplo de Text Area")
janela.geometry("400x300")

# Criar o widget Text (Área de Texto)
text_area = tk.Text(janela, height=10, width=40)
text_area.pack(pady=10)

# Função para obter o conteúdo do Text
def obter_texto():
    conteudo = text_area.get("1.0", tk.END) # Obtém texto a partir da linha 1, coluna 0 até o fim
    print("Conteúdo digitado:")
    print(conteudo)

# Botão para exibir o conteúdo digitado
botao = tk.Button(janela, text="Obter Texto", command=obter_texto)
botao.pack(pady=10)

# Iniciar o loop da interface gráfica
janela.mainloop()