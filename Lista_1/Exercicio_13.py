'''13 - Faze para ti uma arca da madeira de gofer; farás compartimentos na arca e a betumarás por
dentro e por fora com betume. E desta maneira a farás: De trezentos côvados o comprimento
da arca, e de cinquenta côvados a sua largura, e de trinta côvados a sua altura. Farás na arca
uma janela, e de um côvado a acabarás em cima; e a porta da arca porás ao seu lado; far-lhe-ás
andares, baixo, segundo e terceiro. (Gênesis 6:14-16). O côvado é uma unidade de medida usada
na antiguidade. Essa medida equivale ao comprimento do antebraço de um adulto, ou seja, do
cotovelo até a ponta do dedo maior. Ao longo da história, principalmente devido à diferença de
estatura entre os povos, essa medida já representou valores que variam entre 43 a 56
centímetros. Desenvolva um sistema que crie uma média entre os possíveis valores do côvado
e informe a medida da arca em centímetros.'''

soma = ((43+56)*14)/2 #usando a fórmula de progressão aritmética que é: ((a_1+a_n)*n)/2, onde a_1 é o primeiro termo, a_n é o último e n é o número de termos
media = soma/2

medida_comprimento = 300*media
medida_largura = 50*media
area_total = medida_comprimento*medida_largura

print('A arca de Noé tinha {} cm de comprimento, {} cm de largura e {} cm^2 de área toral'.format(medida_comprimento,medida_largura, area_total))