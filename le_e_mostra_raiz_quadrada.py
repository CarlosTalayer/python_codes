### LEIA UM N° E MOSTRE O SEU DOBRO, O TRIPLO E A RAIZ QUADRADA
n1 = int(input('Digite um número inteiro para descobrirmos seu dobro, seu triplo e sua raiz quadrada: '))
d = n1 * 2
t = n1 * 3
r = n1**0.5     # Também pode usar este exemplo: r = pow(n1, 1/2)
print('O dobro do número {} digitado é {}, seu triplo é {} e sua raiz quadrada é {}.' .format(n1, d, t, r))
