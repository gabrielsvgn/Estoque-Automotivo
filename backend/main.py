from banco.conexao import criar_conexao

#Classe carros
class Carro():
    def __init__(self, marca, modelo, ano, cor, quilometragem, preco):
        self.id = None
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem
        self.preco = preco
        self.vendido = True

class Estoque():
    def __init__(self):
        self.conexao = criar_conexao()
        self.cursor = self.conexao.cursor()

    def adicionar_carro(self, carro):
       self.cursor.execute("""
            INSERT INTO carros (marca, modelo, ano, cor, quilometragem, preco, vendido)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
""",        (carro.marca, carro.modelo, carro.ano, carro.cor, carro.quilometragem, carro.preco, carro.vendido))
       self.conexao.commit()

    def listar_carros(self):
       self.cursor.execute("SELECT * FROM carros")
       carros = self.cursor.fetchall()
       for carro in carros:
           print(carro)

    def definir_status(self, id, status):
        for carro in self.carros:
            if carro["ID"] == id:
                carro["status"] = status
                return
    
    def vender_carro(self, id):
            self.definir_status(id, "vendido")
            del self.carro
            self.vendidos.append(self.carro**__dict__)
            
    def marcar_disponível(self, id):
        self.definir_status(id, "disponível")


vectra = Carro("Chevrolet", "Vectra", 2008, "Prata", 186000, 36000)
astra = Carro("Chevrolet", "Astra", 2007, "Vermelho Lyra", 215000, 45000)
estoque = Estoque()
estoque.listar_carros()



