'''Em 1994 aconteceu a primeira final de copa do mundo que foi decidida nos pênaltis. Trinta
anos se passaram e cabe a você desenvolver um sistema que possa relembrar esse
momento. Seu sistema deve simular a disputa de pênaltis entre duas equipes. Para isso, siga
as orientações abaixo:
 Gere dois números inteiros aleatório entre 1 e 10.
 O primeiro número representa o batedor e o segundo o goleiro.
 Se número do batedor for maior que o número do goleiro o pênalti será convertido.

Sabendo-se que cada equipe tem direito a 5 cobranças, informe o nome da equipe vencedora
ou se será necessário iniciar uma rodada de alternâncias.'''
import random

equipe_1 = input('Digite o nome da equipe 1: ')
equipe_2 = input('Digite o nome da equipe 2: ')

pontos_equipe_1 = 0
pontos_equipe_2 = 0

print('__________________|VEZ DA EQUIPE 1|__________________')

batedor_1 = random.randint(1, 10)
goleiro_2 = random.randint(1, 10)
if batedor_1 > goleiro_2:
    print('Gol da equipe {}!'.format(equipe_1))
    pontos_equipe_1 += 1
else:
    print('Goleiro da equipe {} defendeu!'.format(equipe_2))

batedor_1 = random.randint(1, 10)
goleiro_2 = random.randint(1, 10)
if batedor_1 > goleiro_2:
    print('Gol da equipe {}!'.format(equipe_1))
    pontos_equipe_1 += 1
else:
    print('Goleiro da equipe {} defendeu!'.format(equipe_2))

batedor_1 = random.randint(1, 10)
goleiro_2 = random.randint(1, 10)
if batedor_1 > goleiro_2:
    print('Gol da equipe {}!'.format(equipe_1))
    pontos_equipe_1 += 1
else:
    print('Goleiro da equipe {} defendeu!'.format(equipe_2))

batedor_1 = random.randint(1, 10)
goleiro_2 = random.randint(1, 10)
if batedor_1 > goleiro_2:
    print('Gol da equipe {}!'.format(equipe_1))
    pontos_equipe_1 += 1
else:
    print('Goleiro da equipe {} defendeu!'.format(equipe_2))

batedor_1 = random.randint(1, 10)
goleiro_2 = random.randint(1, 10)
if batedor_1 > goleiro_2:
    print('Gol da equipe {}!'.format(equipe_1))
    pontos_equipe_1 += 1
else:
    print('Goleiro da equipe {} defendeu!'.format(equipe_2))
    
print('__________________|VEZ DA EQUIPE 2|__________________')

batedor_2 = random.randint(1, 10)
goleiro_1 = random.randint(1, 10)
if batedor_2 > goleiro_1:
    print('Gol da equipe {}!'.format(equipe_2))
    pontos_equipe_2 += 1
else:
    print('Goleiro da equipe {} defendeu!'.format(equipe_1))

batedor_2 = random.randint(1, 10)
goleiro_1 = random.randint(1, 10)
if batedor_2 > goleiro_1:
    print('Gol da equipe {}!'.format(equipe_2))
    pontos_equipe_2 += 1
else:
    print('Goleiro da equipe {} defendeu!'.format(equipe_1))
    
batedor_2 = random.randint(1, 10)
goleiro_1 = random.randint(1, 10)
if batedor_2 > goleiro_1:
    print('Gol da equipe {}!'.format(equipe_2))
    pontos_equipe_2 += 1
else:
    print('Goleiro da equipe {} defendeu!'.format(equipe_1))

batedor_2 = random.randint(1, 10)
goleiro_1 = random.randint(1, 10)
if batedor_2 > goleiro_1:
    print('Gol da equipe {}!'.format(equipe_2))
    pontos_equipe_2 += 1
else:
    print('Goleiro da equipe {} defendeu!'.format(equipe_1))

batedor_2 = random.randint(1, 10)
goleiro_1 = random.randint(1, 10)
if batedor_2 > goleiro_1:
    print('Gol da equipe {}!'.format(equipe_2))
    pontos_equipe_2 += 1
else:
    print('Goleiro da equipe {} defendeu!'.format(equipe_1))

if pontos_equipe_1>pontos_equipe_2:
    print('A equipe vencedora foi {} com {} gols, e a equipe {} teve {} gols'.format(equipe_1, pontos_equipe_1, equipe_2, pontos_equipe_2))

elif pontos_equipe_1<pontos_equipe_2:
    print('A equipe vencedora foi {} com {} gols, e a equipe {} teve {} gols'.format(equipe_2, pontos_equipe_2,equipe_1, pontos_equipe_1))
else:
    print('__________|EMPATE RODADA DE DESEMPATE|__________')
    batedor_1 = random.randint(1, 10)
    goleiro_2 = random.randint(1, 10)
    if batedor_1 > goleiro_2:
        print('Gol da equipe {}!'.format(equipe_1))
        pontos_equipe_1 += 1
    else:
        print('Goleiro da equipe {} defendeu!'.format(equipe_2))
        
    batedor_2 = random.randint(1, 10)
    goleiro_1 = random.randint(1, 10)
    if batedor_2 > goleiro_1:
        print('Gol da equipe {}!'.format(equipe_2))
        pontos_equipe_2 += 1
    else:
        print('Goleiro da equipe {} defendeu!'.format(equipe_1))
    
    if pontos_equipe_1>pontos_equipe_2:
        print('A equipe vencedora foi {} com {} gols, e a equipe {} teve {} gols'.format(equipe_1, pontos_equipe_1, equipe_2, pontos_equipe_2))

    elif pontos_equipe_1<pontos_equipe_2:
        print('A equipe vencedora foi {} com {} gols, e a equipe {} teve {} gols'.format(equipe_2, pontos_equipe_2,equipe_1, pontos_equipe_1))
    else:
        print('Continua no empate, reinicie a rodada de desempate')