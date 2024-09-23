'''9 - Os diferentes estados físicos da água podem ser observados, naturalmente, no nosso planeta.
A água dos rios e mares, por exemplo, está no estado líquido. Já a água das geleiras está no
estado sólido, e, na atmosfera, encontramos a água no estado gasoso. Frequentemente essa
substância pode mudar de um estado físico para outro a depender de fatores como a

temperatura e a pressão. Sabendo-se que em temperatura inferior a 0° celsius a água encontra-
se no estado solido. Já quando a temperatura se encontra entre 0° e 100° celsius, a água

encontra-se no estado líquido. Por fim, quando a temperatura é superior à 100°, a água
encontra-se no estado gasoso. Faça um programa que leia a temperatura da água e informe o
estado da mesma.'''

temperatura = float(input('Informe a temperatura atual da água: '))

if temperatura < 0:
    print('A água se encontra no estado sólido a {} graus celsius'.format(temperatura))

elif temperatura >= 0 and temperatura <= 100:
    print('A água se encontra no estado líquido a {} graus celsius'.format(temperatura))
    
else:
    print('A água se encontra no estado gasoso a {} graus celsius'.format(temperatura))