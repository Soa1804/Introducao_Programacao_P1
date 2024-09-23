'''15 – Fazer um programa que leia a idade de uma pessoa e informe se a mesma já poderá tirar a
habilitação e o título de eleitor, apenas o título de eleitor ou nenhum dos dois.'''

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você pode tirar habilitação e título de eleitor')

elif idade == 16 or idade == 17:
    print('Você só pode tirar o título de eleitor')
    
else:
    print('Você não pode retirar nenhum dos dois, espere mais um pouco')