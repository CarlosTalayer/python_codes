#Crie um programa que leia um n° real (número com vírgula) e mostre na tela somente a sua parte inteira

from math import trunc # Como vai usar somente o trunc, importa-se somente ele.

num = float(input('Digite um número real. (Ex: 453.27) - Pode digitar: '))
print('O valor digitado foi {} e sua porção inteira é {}.' .format(num, trunc(num))) # O comando trunc só mostra a parte inteira do número.
#ou pode também fazer sem importação da biblioteca math
#num float(input('Digite um valor: '))
#print('O valor digitado foi {} e sua porção inteira é {}.' .format(num, int(num)))
