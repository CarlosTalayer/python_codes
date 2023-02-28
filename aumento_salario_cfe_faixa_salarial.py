# Aumento de salário conforme faixa salarial
sal = float(input('Qual é o salário do funcionário? '))
aum_a = sal * 15 / 100 # Aumento de 15% no salário
aum_b = sal * 10 / 100 # Aumento de 10% no salário
if sal <= 1250:
    print('Este salário teve um aumento de 15% e agora é R$ {:.2f}.' .format(sal + aum_a))
    print('Ou seja, aumentou o valor de R$ {:.2f}.' .format(sal * 15 / 100))
else:
    print('Este salário teve um aumento de 10% e será R$ {:.2f}.' .format(sal + aum_b))
    print('Ou seja, este salário aumentou R$ {:.2f}.' .format(sal * 10 / 100))
