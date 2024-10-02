'''6 - O triângulo retângulo é uma figura geométrica formada por três lados. Ele possui um ângulo
reto, cuja medida é de 90°, e dois ângulos agudos, menores que 90°. Pitágoras, que foi um
filósofo, matemático, astrônomo e músico grego pré-socrático. Nasceu na ilha de Samos no ano
aproximado de 570 a.C. e morreu, provavelmente, em 496 a.C.. Foi um exímio geômetra,
deixando como principal contribuição para a Matemática a descoberta da relação de igualdade
entre o quadrado da hipotenusa e a soma dos quadrados dos catetos no interior de um triângulo
retângulo, o que ficou conhecido como teorema de Pitágoras. Sendo assim, utilizando o teorema
de Pitágoras faça um programa que leia três valores inteiros e informe se foram um triângulo
retângulo.'''

#Condição para ser um triângulo retangulo a^2 = b^2 + c^2

'''hipotenusa = int(input('Digite o valor do maior lado do triângulo: '))
cateto1 = int(input('Digite um segundo valor: '))
cateto2 = int(input('Digite o último valor: '))

quadrado_hipotenusa = hipotenusa**2
quadrado_cateto1 = cateto1**2
quadrado_cateto2 = cateto2**2

if quadrado_hipotenusa == quadrado_cateto1 + quadrado_cateto2:
    print('O triângulo informado é retângulo')

else:
    print('O triângulo informado não é retângulo')'''

valor_1 = float(input('Digite o valor do primeiro lado do triângulo: '))
valor_2 = float(input('Digite um segundo valor: '))
valor_3 = float(input('Digite o último valor: '))

if((valor_1>valor_2)and(valor_1>valor_3)):
    hipotenusa = valor_1
    cateto1 = valor_2
    cateto2 = valor_3

elif((valor_2>valor_1)and(valor_2>valor_3)):
    hipotenusa = valor_2
    cateto1 = valor_1
    cateto2 = valor_3

else:
    hipotenusa = valor_3
    cateto1 = valor_1
    cateto2 = valor_2

quadrado_hipotenusa = hipotenusa*hipotenusa
quadrado_cateto1 = cateto1*cateto1
quadrado_cateto2 = cateto2*cateto2

if quadrado_hipotenusa == quadrado_cateto1 + quadrado_cateto2:
    print('O triângulo informado é retângulo')

else:
    print('O triângulo informado não é retângulo')