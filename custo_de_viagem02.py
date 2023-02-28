# Custo da viagem - com código simplificado
dist = float(input('Qual a distância da sua viagem? '))
print('Só um momento, vou calcular...')
print('Na distância de {} km.' .format(dist))
print('O valor da sua passagem na distância de {} km será de R$ {}.' .format(dist, dist * 0.50 if (dist <= 200) else dist * 0.45))
