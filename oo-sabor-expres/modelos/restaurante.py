class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    def __str__(self):
        return self.nome


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Massas')
restaurante_sushi = Restaurante('Sushi House', 'Japonesa')
restaurante_churrasco = Restaurante('Fogo & Brasa', 'Churrascaria')
restaurante_vegano = Restaurante('Green Life', 'Vegano')

restaurantes = [restaurante_praca, restaurante_pizza, restaurante_sushi, restaurante_churrasco, restaurante_vegano]

for restaurante in restaurantes:
    print(f'Nome: {restaurante.nome}, | Categoria: {restaurante.categoria} | Ativo?: {restaurante.ativo}')