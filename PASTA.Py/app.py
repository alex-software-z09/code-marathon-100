from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

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

bistro_paris.receber_avaliacao('josé', 5)
bistro_paris.receber_avaliacao('gentileza', 3)
bistro_paris.receber_avaliacao('madu', 1)
bistro_paris.receber_avaliacao('china', 4)
bistro_paris.receber_avaliacao('barbara', 2)
bistro_paris.receber_avaliacao('fladysson', 5)

arroz = Prato('Arroz Branco', 30.30, 'Arroz Bom e Barato')
feijão = Prato('Feijão', 30.30, 'Feijão Bom e Barato')
coca = Bebida('Coquinha', 50.00, 'Coca gelada tricando')
bistro_paris.adicionar_no_cardapio(feijão)
bistro_paris.adicionar_no_cardapio(arroz)
bistro_paris.adicionar_no_cardapio(coca)



Restaurante.listar_restaurantes()
Restaurante.mostrar_cardapio(Restaurante)