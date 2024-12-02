from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Zocafood', 'Italiano')
bebida_refri = Bebida('Coca-Zero', 5.0,'grande')
bebida_refri.aplicar_desconto()
prato_pizza = Prato('Pizza',15.00,'Fatia de pizza de calabresa')
prato_pizza.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_refri)
restaurante_praca.adicionar_no_cardapio(prato_pizza)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
