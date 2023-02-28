# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos kms você percorreu com o carro? ')) #kmr = 0.15 * km
dias = float(input('Quantos dias andou com o carro? ')) #diaria = 60 * dias
print('Pelos {:.2f} km percorridos e por {:.2f} diárias, o valor é de R$ {:.2f}.' .format(km, dias, ((0.15 * km) + (60 * dias))))
#ou
#faça a fórmula da seguinte maneira: ---> pago = (0.15 * km) + (60 * dias)
#print('Pelos {:.2f} km percorridos e por {:.2f} diárias, o valor é de R$ {:.2f}.' .format(km, dias, (pago)))
