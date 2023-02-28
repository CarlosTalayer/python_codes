# Primeira e última ocorrência de uma string

frase = str(input('Digite uma frase: ')).upper().strip() # O .upper indicado aqui vai jogar todas as letras "a" para maiúsculas. O .strip corta os espaços.
print('A letra A aparece {} vezes na frase.' .format(frase.count('A'))) # O ".count" conta o n° de vezes que a letra 'A' aparece numa frase.
print('A primeira letra A apareceu na posição {}.' .format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.' .format(frase.rfind('A')+1)) # O recurso 'rfind' procura a letra solicitada da direita para a esquerda.
# O "+1" é indicado para mostrar a posição exata da letra na frase. Lembrando que começa sempre na posição "0" (zero).
