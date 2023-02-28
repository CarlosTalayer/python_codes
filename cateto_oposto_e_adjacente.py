### Lê O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA.
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
#hipotenusa = (num1 ** 2) + (num2 ** 2)
print('A soma do cateto oposto {} e do cateto adjacente {} da hipotenusa é de {:.2f} metros.' .format(co, ca, hi))
#print('A soma dos cateto oposto {} e o cateto adjacente {} dá o comprimento da hipotenusa em {} metros.' .format(num1, num2, hipotenusa))
