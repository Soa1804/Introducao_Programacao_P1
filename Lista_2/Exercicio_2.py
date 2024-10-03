'''2 - No antigo Egito existiram intermináveis conflitos. Sendo uma civilização rica na agricultura
e com forte exército, o Egito encontrava-se na mira de conquistadores. Quase todos repelidos
perante o forte poder do exército egípcio. A maior ameaça do reino era a própria política
interna. Era uma país governado pelo Faraó, figura que acreditavam ser um deus na terra.
Abaixo do Faraó existia o vizir. Esse era responsável pela administração do reino e respondia
apenas ao Faraó. Muitos consideravam o vizir como o feiticeiro do reino. Historiadores acreditam
que os faraós mais famosos foram Hatshepsut, Tutmés III, Ramsés II, Amenhotep III, Tutancâmon
e Cleópatra. Só que esses ficam em segundo plano diante do poder do faraó Yami. Esse era
querido pelo povo e poderoso no combate. O único que rivalizava com o poder do faraó Yami era
o seu vizir conhecido como Kaiba. Um homem focado em conquistar o trono do faraó. Profecias
afirmavam que se existisse guerra entre os apoiados de Yami e os de Kaiba as consequências
seriam desastrosas. O Egito chegaria ao fim. Objetivando a preservação do povo egípcio, foram
criadas estratégias para que os dois pudessem descobrir o vencedor da disputa, mas sem prejuízo
para o povo. Assim, nasceu um jogo de cartas conhecido como mostro de duelo. Por ser um

protótipo cada duelista teria apenas duas cartas. O faraó utilizou uma carta conhecida como Mago
Negro e outra que invocava um ser com o poder dos raios. Já o vizir utilizou uma carta que
invocava um dragão e outra que invocava um gênio mágico. Sabendo que a primeira disputa foi
entre o Mago e o gênio e a segunda entre o dragão e o ser elétrico da escuridão. Faça um
programa que determine o nível de poder de cada carta e o vencedor do duelo.
PS: Nenhuma carta tem poder inferior a 1000 ou superior a 4000.'''

import random

mago_negro = int(random.randint(1000, 4000))
poder_raios = int(random.randint(1000, 4000))
dragao = int(random.randint(1000, 4000))
genio_magico = int(random.randint(1000, 4000))

farao = 0
vizir = 0

print('DUELO 1: Mago Negro X Gênio Mágico, FIGHT')
if mago_negro > genio_magico:
    print('Mago Negro Venceu!!!')
    farao+=1
elif genio_magico > mago_negro:
    print('Gênio Venceu!!!')
    vizir+=1
else:
    print('Deu empate!!!')

print('DUELO 2: Dragão X Ser Elétrico da escuridão, FIGHT')
if poder_raios > dragao:
    print('Ser Elétrico da escuridão Venceu!!!')
    farao+=1
elif dragao > poder_raios:
    print('Dragão Venceu!!!')
    vizir+=1
else:
    print('Deu empate!!!')
        
if farao > vizir:
    print('Faraó Vencer a batalha com as cartas Mago negro com {} pontos e Invocador de Raios com {} pontos'.format(mago_negro, poder_raios))
elif vizir > farao:
    print('Vizir Vencer a batalha com as cartas Gênio Mágico com {} pontos e Dragão com {} pontos'.format(genio_magico, dragao))
else:
    print('Deu empate!!!')