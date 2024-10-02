'''12 - O salto triplo tem raízes na Grécia antiga, onde os atletas competiam em uma forma
primitiva do esporte nos Jogos Olímpicos da antiguidade. Também existem fontes que ligam a
modalidade à Irlanda antiga, onde os atletas disputavam competições com saltos em datas
remotas antes de Cristo. Uma das provas mais antigas do atletismo olímpico, o salto triplo é
disputado desde a primeira edição dos Jogos modernos em 1896 para os homens e, a partir de
1996, nos Jogos de Atlanta, para as mulheres.
Execução do Salto

 Corrida de Impulso: O atleta começa com uma corrida de aproximação para ganhar
velocidade.
 Primeiro Salto (Hop): O atleta salta da tábua de batida, usando o pé de impulsão para
decolar e aterrissar com o mesmo pé.
 Segundo Salto (Step): O atleta realiza um segundo salto, desta vez aterrissando com o
pé oposto.
 Terceiro Salto (Jump): O atleta faz o terceiro salto, aterrissando com ambos os pés na
caixa de areia.
Nesta questão iremos simular uma disputa digital de salto triplo. Desta forma, leia o nome de
dois competidores e informe quem venceu a disputa. Para isso, cada competidor irá informar
um número inteiro qualquer. O sistema irá gerar três números inteiro menores que 100. Se o
primeiro número gerado for da mesma natureza do número indicado pelo usuário (par ou ímpar)
e o segundo número for de natureza contrária o salto será considerado válido caso contrário o
competidor queimou o salto. Vence a competição aquele que obtiver maior número no terceiro
salto e que não tenha queimado as etapas anteriores.'''

'''import random

def verificar_natureza(num):
    return "par" if num % 2 == 0 else "ímpar"

def salto_triplo(nome_competidor):
    numero_usuario = int(input(f"{nome_competidor}, informe um número inteiro: "))
    natureza_usuario = verificar_natureza(numero_usuario)

    # Gerar três números aleatórios menores que 100
    saltos = [random.randint(0, 99) for _ in range(3)]
    print(f"Saltos gerados para {nome_competidor}: {saltos}")

    # Verificar se os saltos são válidos
    if verificar_natureza(saltos[0]) == natureza_usuario:
        print(f"O primeiro salto de {nome_competidor} é válido.")
        if verificar_natureza(saltos[1]) != natureza_usuario:
            print(f"O segundo salto de {nome_competidor} é válido.")
            return saltos[2]  # Retorna o terceiro salto
        else:
            print(f"O segundo salto de {nome_competidor} foi queimado.")
            return -1  # Indica que o competidor queimou o salto
    else:
        print(f"O primeiro salto de {nome_competidor} foi queimado.")
        return -1

# Entradas dos competidores
competidor1 = input("Informe o nome do primeiro competidor: ")
competidor2 = input("Informe o nome do segundo competidor: ")

# Realizar os saltos
resultado1 = salto_triplo(competidor1)
resultado2 = salto_triplo(competidor2)

# Determinar o vencedor
if resultado1 == -1 and resultado2 == -1:
    print("Ambos os competidores queimaram seus saltos.")
elif resultado1 == -1:
    print(f"{competidor2} venceu a competição!")
elif resultado2 == -1:
    print(f"{competidor1} venceu a competição!")
else:
    if resultado1 > resultado2:
        print(f"{competidor1} venceu a competição com um salto de {resultado1}!")
    elif resultado2 > resultado1:
        print(f"{competidor2} venceu a competição com um salto de {resultado2}!")
    else:
        print("Empate!")'''

nome_1 = input('Digite o nome do primeiro participante: ')
nome_2 = input('Digite o nome do segundo participante: ')
numero_1 = int(input("{}, informe um número inteiro: ").format(nome_1))
numero_2 = int(input("{}, informe um número inteiro: ").format(nome_2))
salto_1 = random.randint(1,99)
passou_1 = True
if((numero_1%2==0)and(salto_1%2==0)or(numero_1%2!=0)and(salto_1%2!=0)):
    salto_2 = random.randint(1,99)
    if ((numero_1%1==0)and(salto_2%2==0)or(numero_1%2!=0)and(salto_2%2!=0)):
        salto_3 = random.randint(1,99)
    else:
        print('Queimou o salto 2')
        passou_1 = false
else:
    print('Queimou o salto 1')
    passou_1 = false

passou_2 = True
if((numero_2%2==0)and(salto_1%2==0)or(numero_2%2!=0)and(salto_1%2!=0)):
    salto_2 = random.randint(1,99)
    if ((numero_2%1==0)and(salto_2%2==0)or(numero_2%2!=0)and(salto_2%2!=0)):
        salto_3_2 = random.randint(1,99)
    else:
        print('Queimou o salto 2')
        passou_1 = false
else:
    print('Queimou o salto 1')
    passou_1 = false

if passou_1 and passou_2:
    if salto_3_2<salto_3:
        print('{} venceu').format(nome_1)
    elif salto_3_2>salto_3:
        print('{} venceu').format(nome_2)
    else:
        print('Empate!!!')
elif passou_1:
    print('{} venceu').format(nome_1)
elif passou_2:
    print('{} venceu').format(nome_2)
else:
    print('Nenhum salto valeu')