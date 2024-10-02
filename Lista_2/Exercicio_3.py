'''Fazer um programa que leia um número inteiro positivo e informe se o número lido é
múltiplo de 4 e 8.'''
num = int(input('Digite um número inteiro: '))

if num%4==0 and num%8==0:
    print('O número {} é múltiplo de 4 e 8'.format(num))
elif num%4==0:
    print('O número {} é somente múltiplo de 4'.format(num))
elif num%8==0:
    print('O número {} é somente múltiplo de 8'.format(num))
else:
    print('O número não é múltiplo nem de 4 e nem de 8')