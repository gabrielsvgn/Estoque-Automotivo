from banco.conexao import criar_conexao

class OperacaoBanco:
    def __init__(self):
        self.conexao = criar_conexao()
        self.cursor = self.conexao.cursor()

    def adicionar(self, tabela,carro):
       
       query = f"""
            INSERT INTO {tabela} (marca, modelo, ano, cor, quilometragem, preco)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
       self.cursor.execute(query, (
            carro.marca,
            carro.modelo,
            carro.ano,
            carro.cor,
            carro.quilometragem,
            carro.preco
        ))
       self.conexao.commit()

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