import database as db
class Produtos:
    def cadastrar_produtos(self, nome, qtd_estoque, preco_compra, preco_venda):
        db.cadastrar_podutos_db(nome=nome, qtd=qtd_estoque, p_compra=preco_compra, p_venda=preco_venda)
        return 'Produto Cadastrado'
