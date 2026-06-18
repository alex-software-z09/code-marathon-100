class Restaurante:
    restaurantes = []

    def _init_(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._cardapio = []
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def _str_(self):
        return f'{self._nome} | {self._categoria}'

    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacoes'.ljust(25)} ')
        for restaurante in cls.restaurantes:
            print(f'{Restaurante._nome.ljust(25)} |  {Restaurante._categoria.ljust(25)} | {Restaurante._avaliacoes} ')

    def receber_avaliacao(nome, nota):
        pass

bistro_paris = Restaurante('Bistrô Paris', 'Francesa')
sushi_zen = Restaurante('Sushi Zen', 'Japonesa')
cantina_roma = Restaurante('Cantina Roma', 'Italiana')
burger_king = Restaurante('Burger King', 'Fast Food')
taco_loco = Restaurante('Taco Loco', 'Mexicana')
churrascaria_sul = Restaurante('Churrascaria Pampa', 'Carnes')
vegan_delight = Restaurante('Vegan Delight', 'Vegetariana')
padaria_central = Restaurante('Padaria Central', 'Panificadora')
cafe_amargo = Restaurante('Café Amargo', 'Cafeteria')
sorveteria_gelo = Restaurante('Sorveteria Gelo', 'Sobremesas')
mar_aberto = Restaurante('Mar Aberto', 'Frutos do Mar')
kebab_house = Restaurante('Kebab House', 'Árabe')
thai_spicy = Restaurante('Thai Spicy', 'Tailandesa')
doceria_fina = Restaurante('Doceria Fina', 'Confeitaria')
boteco_esquina = Restaurante('Boteco da Esquina', 'Bar e Petiscos')