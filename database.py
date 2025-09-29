import sqlite3
conn = sqlite3.connect("Estoque_de_vendas.db")
conn.row_factory = sqlite3.Row
crs = conn.cursor()

crs.execute('''
    CREATE TABLE IF NOT EXISTS Produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        qtd_estoque INTEGER NOT NULL,
        preco_compra DOUBLE,
        preco_venda DOUBLE NOT NULL)''')
conn.commit()

def cadastrar_podutos_db(nome, qtd, p_compra, p_venda):
    crs.execute("INSERT INTO Produtos (nome, qtd_estoque, preco_compra, preco_venda) VALUES (?, ?, ?, ?)", (nome, qtd, p_compra, p_venda))
    conn.commit()