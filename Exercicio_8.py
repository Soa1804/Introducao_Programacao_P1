'''8 – Faça um programa que leia o tipo de figura geométrica (retângulo, triângulo ou círculo) e
informe a área da mesma. Obs: Cada figura tem uma forma específica para calcular a área.'''

figura = str(input('Digite a figura que deseja saber a área, retângulo, triângulo ou círculo: '))

if figura == "retângulo" or figura == "retangulo":
    lado = float(input('Digite o valor do lado: '))
    comprimento = float(input('Digite o valor do comprimento: '))
    area = lado * comprimento
    print('A área do seu retângulo é: {:.3f}m^2'.format(area))
    
elif figura == "triângulo" or figura == "triangulo":
    base = float(input('Informe o valor da base: '))
    altura = float(input('Informe o valor da altura: '))
    area = (base * altura)/2
    print('A área do seu triângulo é {:.3f}m^2'.format(area))

elif figura == "círculo" or figura == "circulo":
    raio = float(input('Informe o raio do seu círculo: '))
    area = 3.14 * (raio**2)
    print('Seu círculo tem área {:.3f}m^2'.format(area))

else:
    print('Você não informou a figura corretamente, tente de novo!!!')