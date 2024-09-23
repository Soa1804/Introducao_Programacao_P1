'''1 - Fazer um programa que leia dois números inteiros. Armazene os números lindos nas
variáveis num1 e num2. Se número o número armazenado na variável num2 for par, exiba a
soma dos números lidos, se não, exiba a multiplicação.'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num2 % 2 == 0:
    x = num1 + num2
    print('A soma é: {}'.format(x))

else:
    x = num1 * num2
    print('A multiplicação é: {}'.format(x))