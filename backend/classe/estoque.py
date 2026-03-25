from banco.operacao_banco import OperacaoBanco

class Estoque():

    def adicionar_carro(self, carro):
      tabela = 'carros'
      banco = OperacaoBanco()
      banco.adicionar(tabela, carro)

    def excluir_carro(self, id):
        self.cursor.execute("DELETE FROM carros WHERE id = %s", (id,))
        self.conexao.commit()

    def listar_carros(self):
       self.cursor.execute("SELECT * FROM carros")
       carros = self.cursor.fetchall()
       for carro in carros:
           print(carro)

    def alterar_valor(self, novo_valor, id):
        self.cursor.execute("UPDATE carros SET preco = %s WHERE id = %s", (novo_valor, id))
        self.conexao.commit()