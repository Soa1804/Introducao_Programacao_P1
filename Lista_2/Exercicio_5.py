'''Sabendo-se que a distância entre Recife e Petrolina é de 712Km e que existem postos de
pedágio nas cidades de Caruaru e Arcoverde. Faça um programa que informe o valor pago
em pedágio por um viajante que saiu de Recife com destino a uma das cidades citadas.'''
#pedagio em Caruaru é R$5,75 e em Arcoverde é R$4,65
caruaru = float(input('Informe o valor do pedágio de Caruaru: '))
arcoverde = float(input('Informe o valor do pedágio de Arcoverde: '))

valor_a_pagar = 2*(caruaru + arcoverde)
print('Sabendo que os pedágios em Caruaru é R${} e em Arcoverde é R${},'.format(caruaru, arcoverde)+ 
    'o valor pago juntando a ida e volta foi de: R${}'.format(valor_a_pagar))