# Modo simplificado do exercício

print('Eu escolhi um número de 0 a 5. Tente descobrir qual é.')
num = int(input('Digite o número: '))
print(input('PARABÉNS! Você acertou.' if (num ==3) else 'Aahhh, que pena, você errou! O número que eu havia pensado era o número {}.' .format(3)))
