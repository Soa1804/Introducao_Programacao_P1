'''7 – Triângulo é um polígono de três lados e três ângulos. Há sete tipos de triângulos e sua
classificação depende da disposição dos ângulos podendo ser: isósceles, equilátero, escaleno,
retângulo, obtuso, agudo ou equiângulo. Para uma figura geométrica ser considerada um
triângulo é necessário que a mesma possua três lados e que o valor de um lado isolado não seria
maior do que a soma dos outros dois lados. Ex: (Lado_a = 2, Lado_b = 3, Lado_c = 4) forma um
triângulo; . Ex2: (Lado_a = 12, Lado_b = 3, Lado_c = 4) não forma um triângulo; Faça um
programa que leia três valores inteiros. Informe se esses valores forma um triângulo. Caso
forme, informe que tipo de triângulo foi formado: isósceles, equilátero ou escaleno.'''

lado_a = float(input('Digite o valor do primeiro lado: '))
lado_b = float(input('Digite o valor do segundo lado: '))
lado_c = float(input('Digite o valor do terceito lado: '))

if ((lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_b)):
    print('Essas três retas podem formar um triângulo')
    if (lado_a==lado_b and lado_b==lado_c):
        print('O triângulo é equilátero!')
    elif (lado_a==lado_b and lado_a!=lado_c) or (lado_a==lado_c and lado_a!=lado_b):
        print('O triângulo é isósceles!')
    else:
        print('O triângulo é escaleno')
else:
    print('Essas retas não formam um triângulo')