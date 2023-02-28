### LÊ O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO.
print('Quer ganhar um desconto no produto que irá comprar?')
valor = float(input('Qual o valor do produto? R$ '))
calc = valor * (5 / 100)
#ou
#desc = valor - calc
print('O desconto de 5% diminui R$ {:.2f} no valor do produto. Ficando o valor em R$ {:.2f}.' .format(calc, valor - calc))
#ou
#print('O valor do produto escolhido com o desconto de 5% fica em R$ {}.' .format(desc))
