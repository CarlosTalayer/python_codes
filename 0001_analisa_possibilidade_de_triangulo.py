# Lê valores e analise se pode formar um triângulo
# \033[STYLE;COR DO TEXTO;COR DO FUNDOm
print('\033[1;30;43m-=\033[m' * 14)
print('|\033[1;31;40m     Analisador de Triângulos    \033[m|')
print('\033[1;30;43m-=\033[m' * 14)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
