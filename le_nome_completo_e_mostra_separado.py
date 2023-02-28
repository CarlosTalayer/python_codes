# Lê um nome completo de uma pessoa e mostra o primeiro e último nome separadamente.

n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split() # Com o ".split" eu divido cada palavra do nome em partes
print('Muito prazer em te conhecer!')
print('O seu primeiro nome é {} e seu último sobrenome é {}.' .format(nome[0], nome[len(nome)-1]))
#ou
#print('O seu primeiro nome é {}.' .format(nome[0]))
#print('O seu último nome é {}.' .format(nome[len(nome)-1]))

# Pedindo "len" de nome eu vou saber quantas posições tem nome
# com o "nome[len(nome)-1]" eu solicito que o programa me informe o tamanho do nome menos 1, ou seja, ele retira a primeira posição que
# é a zero e me informa o último nome da lista nome.
