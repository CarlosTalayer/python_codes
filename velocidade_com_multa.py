# Velocidade e multa com código reduzido.
vel = float(input('Digite a velocidade de um carro: '))
print(input('Parabéns, você está no limite de velocidade permitida.' if (vel <= 80) else 'Você ultrapassou o limite, e a multa será de R$ {}.' .format((vel - 80) * 7)))
