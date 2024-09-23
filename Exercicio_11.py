'''11 – Fazer um programa que leia um valor monetário em real e informe o mesmo valor em dólar
e Euro.'''

real = float(input('Digite o valor em reais: '))
dolar = real * 5.51
euro = real * 6.16

print('Seu valor em real é: R${}, em dólar é: ${} e em euro é: €{}'.format(real, dolar, euro))