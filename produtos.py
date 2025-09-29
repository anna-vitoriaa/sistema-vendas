import database as db
class Produtos:
    def cadastrar_produtos(self, nome, qtd_estoque, preco_compra, preco_venda):
        db.cadastrar_podutos_db(nome=nome, qtd=qtd_estoque, p_compra=preco_compra, p_venda=preco_venda)
        return 'Produto Cadastrado'
    
    def vender(self, produto_id, qtd, data):
        db.executar_venda(prod_id= produto_id, qtd= qtd, data= data)
        return 'Venda realizada'