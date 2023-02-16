# Código que pede a pessoa para digitar um nome, e depois o próprio programa escolhe um dos nomes escolhidos.
from random import choice

print('Sorteio do aluno que irá apagar o quadro.')
print('-' * 50) # Aplica 50 hífens para dar um grau
lista = [] #Lista começa vazia
for c in range(1, 5): # define o n° de alunos
    aluno = input(f'Digite o nome do {c}° aluno: ')
    lista. append(aluno) # Adiciona cada um dos alunos digitados ou informados na lista.
aluno_sorteado = choice(lista)
print('O aluno sorteado para apagar o quadro é: {}.' .format(aluno_sorteado))
#ou substitua pelo o código print abaixo
#print(f'O aluno sorteado é: {aluno_sorteado}.')
