### LÊ UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESTE ÂNGULO.
import math
ang = float(input('Digite o ângulo que você deseja, pode ser 30°, 45°, 60° ou 90° ou qualquer outro valor: '))
seno = math.sin(math.radians(ang))
print('O ângulo de {}° tem o seno de {:.2f}.' .format(ang, seno))
cosseno = math.cos(math.radians(ang))
print('O ângulo de {}° tem o cosseno de {:.2f}.' .format(ang, cosseno))
tangente = math.tan(math.radians(ang))
print('O ângulo de {}° tem a tangente de {:.2f}.' .format(ang, tangente))

