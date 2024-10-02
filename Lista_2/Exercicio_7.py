'''Já brincou de pedra, papel e tesoura? Vamos fazer uma rodada dessa brincadeira?
Desenvolva um sistema que possa ler o nome de dois jogadores e informar quem venceu a
rodada ou se existiu um empate.'''

jogador_1 = input('Jogador 1 digite seu nome: ')
jogador_2 = input('Jogador 2 digite seu nome: ')
jogador_1_joga = int(input('Jogador 1 escolha pedra(1), papel(2) ou tesoura(3): '))
jogador_2_joga = int(input('Jogador 2 escolha pedra(1), papel(2) ou tesoura(3): '))

if(jogador_1_joga==1 and jogador_2_joga==1):
    print('Deu empate!!!')
elif(jogador_1_joga==1 and jogador_2_joga==2):
    print('O vencedor foi {}'.format(jogador_2))
elif(jogador_1_joga==1 and jogador_2_joga==3):
    print('O vencedor foi {}'.format(jogador_1))


elif(jogador_1_joga==2 and jogador_2_joga==1):
    print('O vencedor foi {}'.format(jogador_1))
elif(jogador_1_joga==2 and jogador_2_joga==2):
    print('Deu empate!!!')   
elif(jogador_1_joga==2 and jogador_2_joga==3):
    print('O vencedor foi {}'.format(jogador_2))


elif(jogador_1_joga==3 and jogador_2_joga==1):
    print('O vencedor foi {}'.format(jogador_2))
elif(jogador_1_joga==3 and jogador_2_joga==2):
      print('O vencedor foi {}'.format(jogador_1))
elif(jogador_1_joga==3 and jogador_2_joga==3):
    print('Deu empate!!!')

else:
    print('Um dos jogadores ou os dois não escolheram um número válido')