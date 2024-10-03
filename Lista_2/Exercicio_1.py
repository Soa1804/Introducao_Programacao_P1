'''1 - Certo Instituto Federal estava sofrendo com ataques de seres estranhos durante as noites
do final de semana. Depois de muitos sustos decidiu-se contratar especialistas para averiguar
o problema. Foram chamados os caças fantasmas, os irmãos winchester e Dr. Van Helsing.
Os caças fantasmas identificaram que o problema era uma invasão de boneco de machimelo
e que os feixes de prótons poderiam capturar todos, mas o custo seria de 350 reais por cada
boneco encontrado. Já os irmãos winchester falaram que o instituto foi construído em um
antigo cemitério e que os mortos estão levantando para estudar. A solução seria queimar
cada túmulo. No entanto, seriam gastos 120 reais com cada túmulo queimado. Por fim, Van
Helsing falou que era caso de vampiros que passavam a noite nos galhos das árvores
transformados em morcegos esperando sangue. A solução seria colocar alho em todas as
árvores que tenha morcego. O custo seria de 50 reais por cada árvores. Diante de tudo que
foi passado pedimos a uma aluna para vigiar o instituto durante uma noite. Essa menina, tinha
no seu cinto um sistema com três botões. O botão número 1 deveria se apertado se encontrar
boneco de machimelo, o botão de número 2 deveria ser apertado se encontrar algum túmulo,
o botão de número 3 deveria ser apertado quando encontrar um morcego. A menina passou
a noite vestida de branco e andando pelo instituto e pressionou o botão 4 vezes. Agora é com
você informe quanto a escola gastou durante a semana.'''
print('Aperte invasão de boneco de machimelo(1), mortos estão levantando(2) ou morcego(3)')
aperto_1 = int(input('Digite o número do botão apertado a primeira vez: '))
aperto_2 = int(input('Digite o número do botão apertado a segunda vez: '))
aperto_3 = int(input('Digite o número do botão apertado a terceira vez: '))
aperto_4 = int(input('Digite o número do botão apertado a quarta vez: '))

botao_1 = 0
botao_2 = 0
botao_3 = 0

if aperto_1 == 1:
    botao_1+=1
elif aperto_1 == 2:
    botao_2+=1
elif aperto_1 == 3:
    botao_3+=1
else:
    print('infelizmente foi apertado um número diferente dos que são permitidos. Tente de novo!')
    
if aperto_2 == 1:
    botao_1+=1
elif aperto_2 == 2:
    botao_2+=1
elif aperto_2 == 3:
    botao_3+=1
else:
    print('infelizmente foi apertado um número diferente dos que são permitidos. Tente de novo!')
    
if aperto_3 == 1:
    botao_1+=1
elif aperto_3 == 2:
    botao_2+=1
elif aperto_3 == 3:
    botao_3+=1
else:
    print('infelizmente foi apertado um número diferente dos que são permitidos. Tente de novo!')

if aperto_4 == 1:
    botao_1+=1
elif aperto_4 == 2:
    botao_2+=1
elif aperto_4 == 3:
    botao_3+=1
else:
    print('infelizmente foi apertado um número diferente dos que são permitidos. Tente de novo!')
    
valor_total= 350*botao_1 + 120*botao_2 + 50*botao_3

print('O valor total foi de R${}'.format(valor_total))