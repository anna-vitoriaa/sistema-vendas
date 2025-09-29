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

crs.execute('''
        CREATE TABLE IF NOT EXISTS Vendas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER,
            qtd_vendida INTEGER,
            data TEXT,
            )''')
conn.commit()

def cadastrar_podutos_db(nome, qtd, p_compra, p_venda):
    crs.execute("INSERT INTO Produtos (nome, qtd_estoque, preco_compra, preco_venda) VALUES (?, ?, ?, ?)", (nome, qtd, p_compra, p_venda))
    conn.commit()

def executar_venda(prod_id, qtd, data):
    crs.execute('INSERT INTO Vendas(produto_id, qtd_vendida, data) VALUES (?, ?, ?)', (prod_id, qtd, data))
    conn.commit()
    qtd_old = crs.execute('SELECT qtd_estoque FROM Produtos WHERE id= ?', prod_id)
    qtd_new = qtd_old.fetchone()[0]-qtd

    crs.execute('UPDATE Produtos SET qtd_estoque= ? WHERE id= ?', (qtd_new, prod_id))
    conn.commit()