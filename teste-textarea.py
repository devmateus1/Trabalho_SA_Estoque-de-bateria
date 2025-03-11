def buscar_produto(nome_produto):
    conn = sqlite3.connect("produtos.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos WHERE nome LIKE ?", ('%' + nome_produto + '%',))
    resultados = cursor.fetchall()

    conn.close()

    return resultados

    # Exemplo de busca
nome = input("Digite o nome do produto: ")
produtos_encontrados = buscar_produto(nome)

if produtos_encontrados:
    for produto in produtos_encontrados:
        print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: R${produto[2]:.2f}")
    else:
        print("Nenhum produto encontrado.")