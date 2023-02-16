#Digita nome de alunos e sorteia aleatoriamente depois de informar os nomes.
import random

print('Sorteio do aluno que irá apagar o quadro.')
name1 = input('Coloque o nome do primeiro aluno: ')
name2 = input('Coloque o nome do segundo aluno: ')
name3 = input('Coloque o nome do terceiro aluno: ')
name4 = input('Coloque o nome do quarto aluno: ')
lista = (name1, name2, name3, name4)
print('O aluno sorteado para apagar o quadro é: {}.' .format(random.choice(lista)))
