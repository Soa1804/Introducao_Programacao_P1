'''O jogo da vida é um jogo de tabuleiro no qual os jogadores sorteiam a profissão que
seguirão durante toda a partida. Cada profissão tem um salário específico que será entregue
ao jogador cada vez que chegar o dia do pagamento. Contudo, existe a cobrança de imposto
e muitas vezes o jogador receberá o salário pela metade. Neste jogo, o jogador escolherá um
dos dois caminhos possíveis para concluir a partida. No caminho A receberá o pagamento 30
vezes, mas dos 30 dez serão pagos pela metade. Já o caminho B receberá o pagamento 25
vezes, mas dos 25 cinco serão pagos pela metade. Considerando que não existem mais
despesas ou lucros durante o restante do jogo, informe o montante final do jogador.
OBS: O sistema receberá como dado de entrada a profissão sorteada pelo jogador. De acordo
com a tabela abaixo:

Salário do Jogo da Vida
Médico R$50,00
Jornalista R$24,00
Advogado R$50,00
Professor R$24,00
Físico R$30,00
Comerciante R$12,00
Estudante R$16,00'''

import random

print('Sua profissão será médico se tirar 1, jornalista se for 2, advogado se for 3, professor se for 4,'+
        ' físico se for 5, comerciante se for 6, e estudante se for 7')
profissao = int(random.randint(1, 7))

if profissao == 1:
    print('Sua profissão será Médico!')
    caminho = int(input('escolha o caminho A(1) ou B(2): '))
    if caminho == 1:
        salario = 50*(30-10)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))
    else:
        salario = 50*(25-5)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))

elif profissao == 2:
    print('Sua profissão será Jornalista!')
    caminho = int(input('escolha o caminho A(1) ou B(2): '))
    if caminho == 1:
        salario = 24*(30-10)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))
    else:
        salario = 24*(25-5)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))
    
elif profissao == 3:
    print('Sua profissão será Advogado!')
    caminho = int(input('escolha o caminho A(1) ou B(2): '))
    if caminho == 1:
        salario = 50*(30-10)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))
    else:
        salario = 50*(25-5)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))
        
elif profissao == 4:
    print('Sua profissão será Professor!')
    caminho = int(input('escolha o caminho A(1) ou B(2): '))
    if caminho == 1:
        salario = 24*(30-10)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))
    else:
        salario = 24*(25-5)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))

elif profissao == 5:
    print('Sua profissão será Físico!')
    caminho = int(input('escolha o caminho A(1) ou B(2): '))
    if caminho == 1:
        salario = 30*(30-10)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))
    else:
        salario = 30*(25-5)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))

elif profissao == 6:
    print('Sua profissão será Comerciante!')
    caminho = int(input('escolha o caminho A(1) ou B(2): '))
    if caminho == 1:
        salario = 12*(30-10)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))
    else:
        salario = 12*(25-5)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))

else:
    print('Sua profissão será Estudante!')
    caminho = int(input('escolha o caminho A(1) ou B(2): '))
    if caminho == 1:
        salario = 16*(30-10)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))
    else:
        salario = 16*(25-5)
        print('Seu salário será de após os impostos serem cobrados: R${}'.format(salario))