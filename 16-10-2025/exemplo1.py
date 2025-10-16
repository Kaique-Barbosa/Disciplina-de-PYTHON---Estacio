import sqlite3 as sql

#criação de lista de strings sql
strings_sql= [
    """ 
     CREATE TABLE IF NOT EXISTS PRODUTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME TEXT NOT NULL,
        QUANTIDADE INTERGER,
        PRECO REAL
    )
    """,
    """
        INSERT INTO PRODUTOS (NOME, QUANTIDADE, PRECO)  VALUES (?, ?, ?)
    """,
    """ UPDATE produtos SET quantidade = ? WHERE id = ? """,
    """
        DELETE FROM PRODUTOS where id = ?;
    """,
    "SELECT * FROM PRODUTOS ORDER BY nome DESC",
]


#conexao para o banco

conn = sql.connect('ESTOQUE.db')

#criação da tabela "PRODUTOS"

conn.cursor().execute(strings_sql[0])

#CRUD: 
#INCLUSAO:
conn.cursor().execute(strings_sql[1], ['Parafuso', 100, 1.25])
conn.commit()

#alteração
conn.cursor().execute(strings_sql[2], [21, 5])
conn.commit()

#exclusao
conn.cursor().execute(strings_sql[3], [2,])
conn.commit()

#LISTAGENS
lista_produtos = conn.cursor().execute(strings_sql[4]).fetchall()

for produto in lista_produtos:
    print(produto)
