### LÊ UM VALOR EM METROS E CONVERTE PARA CENTÍMETROS E MILÍMETROS
medida = float(input('Digite uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('O valor de {} em metros digitado corresponde a {:.0f} centímetros e {:.0f} milímetros.' .format(medida, cm, mm))
