from avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
 
    def __init__(self, nome, categoria):
        self._nome = nome.title() 
        self._categoria = categoria.upper()
        self._cardapio = []
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    def listar_restaurantes(cls): 
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliações'.ljust(25)}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.media_avaliacao} ')

    def receber_avaliacao(self, nome, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(nome,nota)
            self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacao(self):
        soma = 0
        for avaliacao in self._avaliacoes:
            soma += avaliacao._nota
        try:
            media = soma / len(self._avaliacoes)
            return round(media, 1)
        except ZeroDivisionError:
            return '-'


            def adicionar_no_cardapio(self, opcão):
         if isinstance():
            




