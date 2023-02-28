# Lê um número inteiro e mostra se é PAR ou ÍMPAR
num = int(input('Digite um número e direi a você se ele é PAR ou é ÍMPAR: '))
resultado = num % 2
print('O número {} é PAR.' .format(num) if (resultado == 0) else 'Este número é ÍMPAR')
