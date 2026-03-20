#Classe carros
class Carro():
    def __init__(self, valor, km, ano, cor, marca, modelo, placa, status):
        self.valor = valor
        self.km = km
        self.ano = ano
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.status = status

class Estoque():
    def __init__(self):
        self.carros = []
        self.vendidos = []

    def adicionar_carro(self, carro):
        self.carros.append({
            "ID": len(self.carros) + 1,
            **carro.__dict__
        })

    def listar_carros(self):
        for lista in self.carros:
            print(lista)

    def listar_vendidos(self):
        for carro in self.vendidos:
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


vectra = Carro(36000, "186000", "2008", "prata", "Chevrolet", "Vectra", "DDI0I17", "disponível")
astra = Carro(45000, "215000", "2007", "Vermelho", "Chevrolet", "Astra SS", "IRB7A08", "disponível")
estoque = Estoque()
estoque.adicionar_carro(vectra)
estoque.adicionar_carro(astra)
estoque.vender_carro(1)
estoque.listar_carros()
estoque.listar_vendidos()

