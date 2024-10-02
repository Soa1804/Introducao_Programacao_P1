'''Um senhor esquelético saiu pela cidade em busca de amigos que pudessem ajudar a
abrir uma porta que estava presa. No percurso, passou pelo zoológico que era gerenciado
por um senhor corcunda e muito peludo. Explicou o problema e o mesmo aceitou ajudar.
Seguiram juntos até um ortodontista e lá encontraram um homem de um braço só e que
utilizava aparelho nos dentes. Esse homem, também resolveu ajudar. O trio caminhava em
direção a porta quando apareceu uma mulher de maiô roxo e a mesma disse que gostaria de
ajudar. Disse que era vidente e que conseguia visualizar que todos juntos irão abrir a porta.
Quando chegaram no lugar, viram que era uma porta grande construída a muito tempo

utilizando madeira de carvalho. Com uma corda, começaram a puxar à porta. O que o grupo
não sabia, era que do outro lado morava uma senhora vestida com fantasia de carnaval. Ela
ficou com medo de ser roubada e pediu ajuda a um amigo praticante de musculação. Os dois
segurando a porta para impedindo de abrir. Agora é com você. A porta abriu ou não abriu?
Neste programa, será necessário saber o nível de força de cada membro. Para isso, utilize a
medida F. Exemplo: Uma pessoa normal tem 20F de força. Já um atleta pode chegar a 50F
de força. Pessoas especiais podem ter um nível maior de força.
OBS: A porta abre quando puxada por força superior a 120F.'''

import random

senhor_esqueletico = int(random.randint(20, 50))
corcunda = int(random.randint(20, 50))
homem_um_braco = int(random.randint(20, 50))
maio_roxo = int(random.randint(20, 50))

mulher_carnaval = int(random.randint(20, 50))
homem_musculacao = int(random.randint(20, 50))

quarteto = senhor_esqueletico + corcunda + homem_um_braco + maio_roxo
dupla = mulher_carnaval + homem_musculacao

if (quarteto >= 120) and (quarteto > dupla):
    print('O quarteto conseguiu abrir a porta com uma força total de {}F e a dupla teve {}F'.format(quarteto, dupla))
    
else:
    print('O quarteto não conseguiu abrir a porta com uma força total de {}F e a dupla teve {}F'.format(quarteto, dupla))