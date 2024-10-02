'''2 - Sabendo que a fórmula para calcular o peso ideal é:
➢ Para mulheres: (62.1 * altura) – 44.7;
➢ Para homens: (72.2 * altura) – 58;
Faça um programa que recebe o sexo e a altura de uma pessoa e informe o peso ideal'''
sexo = str(input('Digite o seu sexo, masculino(1) ou feminino(2): '))
altura = float(input('Digite sua altura: '))

if sexo == '1':
    peso_ideal = (72.2 * altura) - 58
    print('Seu peso ideal é: {}'.format(peso_ideal))

elif sexo == '2':
    peso_ideal = (62.1 * altura) - 44.7
    print('Seu peso ideal é: {}'.format(peso_ideal))
else:
    print('Informe um dos valores indicados, tente novamente!!!')