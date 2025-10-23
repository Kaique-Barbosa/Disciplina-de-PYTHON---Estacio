import sqlite3 as db_sqlite3  # Biblioteca nativa do Python para SQLite
from  datetime import datetime as dataAtual

# ------------------------------------------------------

# 1 Conexão com o banco de dados

# ------------------------------------------------------

conexao = db_sqlite3.connect("Estoque.db")

cur = conexao.cursor()

# ------------------------------------------------------

# 2 Lista com todas as strings SQL usadas no sistema

# ------------------------------------------------------

sql_strings = [

    """CREATE TABLE IF NOT EXISTS produto (

        codigo INTEGER PRIMARY KEY AUTOINCREMENT,

        descricao TEXT NOT NULL,

        qt INTEGER NOT NULL,

        preco REAL NOT NULL,

        categoria INTEGER NOT NULL, 

        data TEXT NOT NULL

    )""",

    """INSERT INTO produto (descricao, qt, preco, categoria, data)

       VALUES (?, ?, ?, ?, ?)""",

    """SELECT codigo, descricao, qt, preco, categoria, DATE(data) FROM produto ORDER BY descricao""",

    """UPDATE produto SET descricao=?, qt=?, preco=?, categoria=?

       WHERE codigo=?""",

    """DELETE FROM produto WHERE codigo=?""",

    """SELECT * FROM produto WHERE codigo=?""",

    """SELECT codigo, descricao, qt, preco, categoria

       FROM produto WHERE categoria=?""",

    """ SELECT * FROM produto WHERE descricao LIKE ? """,


]

# Executa o comando de criação da tabela

cur.execute(sql_strings[0])

conexao.commit()
 
# ------------------------------------------------------

# 3 Função: cadastrar_produto()

# ------------------------------------------------------

def cadastrar_produto():

    """Lê dados do usuário e insere novo produto na tabela"""

    print("\n--- Cadastrar Produto ---")

    descricao = input("Descrição: ")

    qt = int(input("Quantidade: "))

    preco = float(input("Preço: "))

    categoria = int(input("Categoria (número): "))

    # Executa a inserção usando a posição [1] da lista de SQL

    cur.execute(sql_strings[1], (descricao, qt, preco, categoria, dataAtual.now()))

    conexao.commit()

    print("✅ Produto cadastrado com sucesso!")


# ------------------------------------------------------

# 4 Função: listar_produtos()

# ------------------------------------------------------

def listar_produtos():

    """Mostra todos os produtos cadastrados"""

    print("\n--- Lista de Produtos ---")

    # Executa a query [2] (listar todos)

    cur.execute(sql_strings[2])

    produtos = cur.fetchall()
  

    if not produtos:

        print("⚠️ Nenhum produto cadastrado.")

        return

    # Exibe cada registro encontrado

    for p in produtos:

        print(f"Código: {p[0]} | Descrição: {p[1]} | Qt: {p[2]} | Preço: R$ {p[3]:.2f} | Categoria: {p[4]} | Data: {p[5]}")


# ------------------------------------------------------

# 5 Função: listar_por_categoria()

# ------------------------------------------------------

def listar_por_categoria():

    """Permite filtrar produtos de uma categoria específica"""

    print("\n--- Listar Produtos por Categoria ---")

    cat = int(input("Informe o número da categoria: "))

    # Executa o comando SQL [6]

    cur.execute(sql_strings[6], (cat,))

    produtos = cur.fetchall()

    if not produtos:

        print("⚠️ Nenhum produto encontrado nessa categoria.")

        return

    # Exibe cada produto da categoria

    for p in produtos:

        print(f"Código: {p[0]} | Descrição: {p[1]} | Qt: {p[2]} | Preço: R$ {p[3]:.2f} | Categoria: {p[4]}")


# ------------------------------------------------------

# 6 Função: Listar por produtos que contenham na descrição "valor desejado"

# ------------------------------------------------------

def filtrar_por_descricao():

    """Permite filtrar a descrição de um produto que contenha no meio de caracters """

    print("\n--- Pesquise pela descrição desejada ---")

    filtro = input("Informe o nome para realizar a pesquisa: ")
    
    # Executa o comando SQL [7]

    cur.execute(sql_strings[7], ('%' + filtro + '%',))

    produtos = cur.fetchall()

    if not produtos:

        print("⚠️ Nenhum produto encontrado com essa descrição")

        return

    # Exibe cada produto da categoria

    for p in produtos:

        print(f"Código: {p[0]} | Descrição: {p[1]} | Qt: {p[2]} | Preço: R$ {p[3]:.2f} | Categoria: {p[4]}")


# ------------------------------------------------------


# 6 Função: atualizar_produto()

# ------------------------------------------------------

def atualizar_produto():

    """Atualiza um produto existente, mantendo valores antigos se o usuário não digitar novos"""

    print("\n--- Atualizar Produto ---")

    codigo = int(input("Código do produto: "))

    # Busca produto pelo código (query [5])

    cur.execute(sql_strings[5], (codigo,))

    produto = cur.fetchone()

    if not produto:

        print("⚠️ Produto não encontrado.")

        return

    # Exibe valores atuais e permite alterar somente os desejados

    descricao = input(f"Nova descrição ({produto[1]}): ") or produto[1]

    qt = input(f"Nova quantidade ({produto[2]}): ") or produto[2]

    preco = input(f"Novo preço ({produto[3]}): ") or produto[3]

    categoria = input(f"Nova categoria ({produto[4]}): ") or produto[4]

    # Executa o comando de atualização (índice [3])

    cur.execute(sql_strings[3], (descricao, int(qt), float(preco), int(categoria), codigo))

    conexao.commit()

    print("✅ Produto atualizado com sucesso!")
 
 
# ------------------------------------------------------

# 7 Função: excluir_produto()

# ------------------------------------------------------

def excluir_produto():

    """Exclui um produto do banco de dados pelo código"""

    print("\n--- Excluir Produto ---")

    codigo = int(input("Código do produto: "))

    # Executa o comando de exclusão (índice [4] da lista sql_strings)

    cur.execute(sql_strings[4], (codigo,))

    conexao.commit()

    print("✅ Produto excluído com sucesso!")
 

# ------------------------------------------------------
# Menu interativo
# ------------------------------------------------------

def menu():
    while True:
        print("\n--- Menu de Opções ---")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Listar Produtos por Categoria")
        print("4 - Filtrar por Descrição")
        print("5 - Atualizar Produto")
        print("6 - Excluir Produto")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            listar_por_categoria()
        elif opcao == '4':
            filtrar_por_descricao()
        elif opcao == '5':
            atualizar_produto()
        elif opcao == '6':
            excluir_produto()
        elif opcao == '0':
            print("Saindo... Até logo!")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")

# Inicia o menu
menu()

# Fechar conexão ao banco de dados ao final

conexao.close()

 