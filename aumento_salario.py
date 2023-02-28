##### LÊ O SALÁRIO DE UM COLABORADOR E ADICIONA UM AUMENTO DE 15%.
sal = int(input('Digitel o seu salário para saber quanto ficará com o aumento de 15%: R$ '))
aum = sal * (15 / 100)
#ou
#valor = sal + aum
print('O salário com o aumento de 15% vai para R$ {:.2f}.' .format(sal + aum))
#ou
#print('O seu salário de R$ {} com o aumento de 15% vai para R$ {}.' .format(sal, valor))
