n = input('Digite qualquer coisa. Pode ser números, palavras com números ou símbolos: ') #Colocando input sempre mostrará como string.
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?' , n.isalnum())
print('Está em minúsculas?', n.islower())
print('Está em maiúsculas?', n.isupper())
print('Está capitalizada', n.istitle())
