'''8 – Faça um programa que leia o tipo de figura geométrica (retângulo, triângulo ou círculo) e
informe a área da mesma. Obs: Cada figura tem uma forma específica para calcular a área.'''

figura = str(input('Digite a figura que deseja saber a área, retângulo(1), triângulo(2) ou círculo(3): '))

if figura == '1':
    lado = float(input('Digite o valor do lado: '))
    comprimento = float(input('Digite o valor do comprimento: '))
    area = lado * comprimento
    print('A área do seu retângulo é: {:.3f}m^2'.format(area))
    
elif figura == '2':
    base = float(input('Informe o valor da base: '))
    altura = float(input('Informe o valor da altura: '))
    area = (base * altura)/2
    print('A área do seu triângulo é {:.3f}m^2'.format(area))

elif figura == '3':
    raio = float(input('Informe o raio do seu círculo: '))
    area = 3.14 * (raio*raio)
    print('Seu círculo tem área {:.3f}m^2'.format(area))

else:
    print('Você não informou a figura corretamente, tente de novo!!!')