### LÊ UM NÚMERO INTEIRO QUALQUER E MOSTRA A SUA TABUADA
num = int(input('Digite um número inteiro qualquer e veremos a sua tabuada até o número 20. \nPor favor digite: '))
print('A tabuada do {} é: ' .format(num))
print('=' * 10) # Coloquei para mostrar linhas antes da tabuada
print('{} x {:2} = {}' .format(num, 1, num * 1)) #Entre as chaves para ficar alinhado coloquei {:2}
print('{} x {:2} = {}' .format(num, 2, num * 2))
print('{} x {:2} = {}' .format(num, 3, num * 3))
print('{} x {:2} = {}' .format(num, 4, num * 4))
print('{} x {:2} = {}' .format(num, 5, num * 5))
print('{} x {:2} = {}' .format(num, 6, num * 6))
print('{} x {:2} = {}' .format(num, 7, num * 7))
print('{} x {:2} = {}' .format(num, 8, num * 8))
print('{} x {:2} = {}' .format(num, 9, num * 9))
print('{} x {} = {}' .format(num, 10, num * 10))
print('=' * 10) # Coloca linhas abaixo da tabuada
