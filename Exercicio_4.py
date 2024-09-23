'''4 - O Sr. Carlos é o melhor pedreiro de WAKANDA. Foi contratado por T’Challa para revestir o
muro frontal que protege o castelo com placas de vibranium. As placas são no formato
quadrangular possuindo 2m em cada lado. Já o muro é no formato retangular, possuindo 100m
de comprimento e 4m de altura. Faça um programa que informe quantas placas de vibranium
serão necessárias para revestir o muro.'''

#Uma placa etm 2mX2m
placa = 4 #já que uma placa é quadrangular com 2 metros de comprimento e 2 metros de largura então o total é 4m^2

#MURO
comprimento = 100
altura = 4
metros_quadrados = comprimento * altura

quantidade_de_placas = metros_quadrados / placa

print('Sr. Carlos irá utilizar {} placas de vibranium'.format(quantidade_de_placas))