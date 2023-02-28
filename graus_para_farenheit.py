### TRANSFORMA GRAUS CELSIUS PARA GRAUS FAHRENHEIT OU VICE-VERSA
cel = float(input('Quer saber quantos graus celsius fica convertido para farenheit? \nDigite quantos graus celsius quer converter para farenheit: '))
far =float(input('Agora digite quantos graus farenheit quer converter para celsius: '))
print('A temperatura de {} °C (graus celsius) convertido para farenheit é {:.2f} °F.' .format(cel, (cel * 1.8) + 32))
print('A temperatura de {} °F convertido para graus celsius é {:.2f}' .format(far, (far - 32) / 1.8))
#far = 32
#formula C° = (graus * 1.8) + 32 -->Formula C° para F°
# ou
# formula C° = 9 * graus / 5 + 32
# formula F°= (graus - 32) / 1.8 --> Fórmula F° para C°
#ou
#f = 9 * c / 5 + 32
