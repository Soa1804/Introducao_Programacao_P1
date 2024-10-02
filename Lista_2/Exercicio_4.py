'''Bart é o filho mais velho de uma família com 5 integrantes. Conforme apresentamos na
figura.

Certo dia foi solicitado que Bart fosse a pastelaria do krusty, pois hoje seria o dia do pastel.
Chegando à pastelaria Bart viu o seguinte Menu:
Pastel | Preço
Carne  | 12,50
Queijo | 10,00
Frango | 11,11
Sabendo-se que cada membro da família come apenas um pastel, informe o valor gasto por
Bart.'''
print('Pastel de carne(1), queijo(2), frango(3)')
escolha_1 = int(input('Digite o número do primeiro pastel pastel l: '))
escolha_2 = int(input('Digite o número do segundo pastel pastel 2: '))
escolha_3 = int(input('Digite o número do terceiro pastel pastel 3: '))
escolha_4 = int(input('Digite o número do quarto pastel pastel 4: '))
escolha_5 = int(input('Digite o número do quinto pastel pastel 5: '))

pasteis = [escolha_1, escolha_2, escolha_3, escolha_4, escolha_5]

carne = 0
queijo = 0
frango = 0

if escolha_1 == 1:
    carne+=1
elif escolha_1 == 2:
    queijo+=1
elif escolha_1 == 3:
    frango+=1
else:
    print('Foi informado um número de pedido inválido, tente de novo!')
    exit()
if escolha_2 == 1:
    carne+=1
elif escolha_2 == 2:
    queijo+=1
elif escolha_2 == 3:
    frango+=1
else:
    print('Foi informado um número de pedido inválido, tente de novo!')
    exit()
if escolha_3 == 1:
    carne+=1
elif escolha_3 == 2:
    queijo+=1
elif escolha_3 == 3:
    frango+=1
else:
    print('Foi informado um número de pedido inválido, tente de novo!')
    exit()
if escolha_4 == 1:
    carne+=1
elif escolha_4 == 2:
    queijo+=1
elif escolha_4 == 3:
    frango+=1
else:
    print('Foi informado um número de pedido inválido, tente de novo!')
    exit()
if escolha_5 == 1:
    carne+=1
elif escolha_5 == 2:
    queijo+=1
elif escolha_5 == 3:
    frango+=1
else:
    print('Foi informado um número de pedido inválido, tente de novo!')
    exit()
    
valor_total = carne*12.50 + queijo*10.00 + frango*11.11

print('O valor final da conta foi de R${} reais'.format(valor_total))