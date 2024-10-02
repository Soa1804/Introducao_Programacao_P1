'''Uma loja virtual lhe contratou para desenvolver o sistema de pagamento. Foi explicado
que existem três formas de pagamento. São elas:
Pix – desconto de 11,11%
Dinheiro – valor normal do produto
Cartão – acréscimo de 3 reais no valor final'''

forma_pagamento = int(input('Escolha a forma de pagamento, sendo Pix(1), Dinheiro(2) e Cartão(3): '))
valor_compra = float(input('Digite o valor total da compra: '))

if forma_pagamento == 1:
    desconto = valor_compra - (valor_compra*(11.11/100))
    print('O valor final a se pagar com o desconto foi de R${}'.format(desconto))

elif forma_pagamento == 2:
    print('O valor final foi o mesmo que o original foi de R${}'.format(valor_compra))
    
elif forma_pagamento == 3:
    acrescimo = valor_compra + 3.00
    print('O valor final a se pagar com o acrescimo foi de R${}'.format(acrescimo))

else:
    print('A forma de pagamento informado foi inválido tente de novo!')