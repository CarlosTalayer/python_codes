#Digita nome dos alunos e sorteia a ordem de apresentação de trabalho dos alunos.

import random

print('Sorteio do aluno que irá apagar o quadro.')
name1 = input('Coloque o nome do primeiro aluno: ')
name2 = input('Coloque o nome do segundo aluno: ')
name3 = input('Coloque o nome do terceiro aluno: ')
name4 = input('Coloque o nome do quarto aluno: ')
lista = (name1, name2, name3, name4)
print('O primeiro aluno sorteado para apresentar o trabalho é: {}, o segundo é {}, o terceiro é {} e o último é {}.' .format(random.choice(lista), random.choice(lista), random.choice(lista), random.choice(lista)))
