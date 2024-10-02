'''10 – Faça um programa que leia dois números e informe o menor número.'''
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
    print('O maior valor é: {}'.format(num1))
    
elif num1 < num2:
    print('O maior valor é: {}'.format(num2))
    
else: 
    print('Os dois tem o mesmo valor sendo ele: {}'.format(num1))