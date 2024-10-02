'''Salto Ornamental é um esporte individual que consiste em saltar de uma plataforma
elevada, fixa ou não (trampolin), em direção a uma piscina, realizando uma série de
movimentos acrobáticos e estéticos. Um dos critérios para vencer a competição é espirar a
menor quantidade de água no processo de mergulho. Três mergulhadores foram para a final.
Utilize seu conhecimento adquirido na disciplina para criar um meio de identificar o vencedor.
OBS: Só poderá utilizar o que foi visto em sala de aula'''
import random

mergulador_1 = random.randint(1,1000)
mergulador_2 = random.randint(1,1000)
mergulador_3 = random.randint(1,1000)

if (mergulador_1<mergulador_2) and (mergulador_1<mergulador_3):
    print('O mergulador 1 venceu tendo espirrado {}ml, enquanto o competidor 2 espirrou {}ml e o mergulador 3 espirrou {}ml'.format(mergulador_1, mergulador_2, mergulador_3))

elif (mergulador_2<mergulador_1) and (mergulador_2<mergulador_3):
    print('O mergulador 2 venceu tendo espirrado {}ml, enquanto o competidor 1 espirrou {}ml e o mergulador 3 espirrou {}ml'.format(mergulador_2, mergulador_1, mergulador_3))
    
else:
    print('O mergulador 3 venceu tendo espirrado {}ml, enquanto o competidor 1 espirrou {}ml e o mergulador 2 espirrou {}ml'.format(mergulador_3, mergulador_1, mergulador_2))