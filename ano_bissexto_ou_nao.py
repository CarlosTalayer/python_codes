# Ano bissexto
from datetime import date
ano = int(input('Que ano você quer saber se é BISSEXTO? Informe para eu analisar, ou coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano %100 != 0 or ano % 400 == 0:
    print(input('O ano {} É BISSEXTO.' .format(ano)))
else:
    print(input('O ano {} NÃO É BISSEXTO.' .format(ano)))
