''' Cwestiynest é um jogo de múltiplas escolha onde o participante escolhe entre as letras A,
B, C, D e E. Esse jogo possui 5 fases e o jogador só irá para fazer seguinte se acerta a
alternativa da fase anterior. Faça um programa que exiba a mensagem “parabéns” para o
jogador que acertou todas as fases e “tente outra vezes” para o jogador que errar uma das
alternativas.'''
import random
alternativa_correta_1 = random.choice(['A', 'B', 'C', 'D', 'E'])
alternativa_correta_2 = random.choice(['A', 'B', 'C', 'D', 'E'])
alternativa_correta_3 = random.choice(['A', 'B', 'C', 'D', 'E'])
alternativa_correta_4 = random.choice(['A', 'B', 'C', 'D', 'E'])
alternativa_correta_5 = random.choice(['A', 'B', 'C', 'D', 'E'])

alternativa_1 = input('Digite uma letra entre A e E: ').upper()

if alternativa_1==alternativa_correta_1:
    print('Parabéns!!!')
    alternativa_2 = input('Digite uma letra entre A e E: ').upper()
    if alternativa_2==alternativa_correta_2:
        print('Parabéns!!!')
        alternativa_3 = input('Digite uma letra entre A e E: ').upper()
        if alternativa_3==alternativa_correta_3:
            print('Parabéns!!!')
            alternativa_4 = input('Digite uma letra entre A e E: ').upper()
            if alternativa_4==alternativa_correta_4:
                print('Parabéns!!!')
                alternativa_5 = input('Digite uma letra entre A e E: ').upper()
                if alternativa_5==alternativa_correta_5:
                    print('Parabéns você venceu!!!')
                elif alternativa_5!=alternativa_correta_5:
                    print('Tente Novamente!!!')
            elif alternativa_4!=alternativa_correta_4:
                print('Tente Novamente!!!')
        elif alternativa_3!=alternativa_correta_3:
            print('Tente Novamente!!!')
    elif alternativa_2!=alternativa_correta_2:
        print('Tente Novamente!!!')
elif alternativa_1!=alternativa_correta_1:
    print('Tente Novamente!!!')

print('As alternativas eram: {}, {}, {}, {} e {}'.format(alternativa_correta_1, alternativa_correta_2, alternativa_correta_3, alternativa_correta_4, alternativa_correta_5))