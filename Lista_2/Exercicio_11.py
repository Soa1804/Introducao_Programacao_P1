'''Um menino chamado Francisco mora no estado de São Paulo, em um sítio nas cercanias
da Vila Abobrinha, no interior do estado. Essa região é de difícil acesso e não existe transporte
escolar e nem energia elétrica. Todos os dias acorda com o cantar do velho galo Altaliba que
não “falha” em cantar ao raiar do sol. Gasta 50 min para caminhar uma légua e meia até
chegar à única escola da região. Por conta da distância, Francisco, filho do Nhô Bento,
sempre chega atrasado à sala de aula. A professora pergunta o motivo e ele explica que saiu
apressado e não deu tempo de calçar a botina que ajudaria a caminhar mais rápido. Chico
fala que quando sai de botina consegue chegar à escola em 40 min e quando vem montando
no Teobaldo esse tempo diminui para 30 min. Dona Marocas, que é a professora da escola,
retruca dizendo que em dias quentes ele para no riacho e por conta disso o tempo para chegar à
escola aumenta em 40 min. Já quando sai sem café da manhã entra no pomar do Nhô Lau,
aumentando em 20 min o tempo para chegar à escola por conta das goiabas que come.
Quando se encontra com Rosinha, aí não tem jeito. Atrasa 10 min por cada troca de ptialina
realizada. O Chico toma a fala já chateado e diz que chega 30 min mais rápido quando é
surpreendido pela onça. Agora é com você. Qual o tempo gasto por Chico para chegar à
escola no dia 07/06/2021.'''

#50 minutos sem botinas
#se usar botina chega em 40 minutos
#quando vem de cavalo leva 30 minutos
#dias quentes leva mais 40 minutos
#sem café leva aumaenta 20 minutos
#10 minutos por trocas de ptialina

print('No dia 07/06/2021, desceva como ele começou até chegar a escola')
botina = int(input('Você calçou a botina? sim(1) ou não(2): '))
cavalo = int(input('Você foi de cavalo? sim(1) ou não(2): '))
dias_quente = int(input('O dia foi quente? sim(1) ou não(2): '))
cafe = int(input('Você tomou café da manhã? sim(1) ou não(2): '))
rosinha = int(input('Você se encontrou com a rosinha? sim(1) ou não(2): '))

tempo_total = 0

if botina == 1:
    tempo_total+=40
else:
    tempo_total+=50    
    
if cavalo == 1:
    tempo_total-=30
else:
    tempo_total+=0 
               
if dias_quente == 1:
    tempo_total+=40
else:
    tempo_total+=0
                
if cafe == 1:
    tempo_total+=0
else:
    tempo_total+=20
    
if rosinha == 1:
    ptialina = int(input('Quantas ptialina vocês trocaram? '))
    total_ptialina = ptialina*10
    tempo_total+=total_ptialina
else:
    tempo_total+=0

print('No dia 07/06/2021 o tempo que Francisco levou foi de {} minutos'.format(tempo_total))
    
