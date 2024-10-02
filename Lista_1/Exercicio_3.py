'''3 - O Senhor Wayne sofreu um acidente de carro na cidade de Metrópolis, a qual visitou para
ser entrevistado por Clark Kent. Pediu a Alfred para levar o carro a funilaria. Nela foi
informado que seria necessárias duas semanas para o conserto. O problema é que nesse
tempo, recebeu uma ligação de Dick Grayson informando um sinal luminoso no céu de
Gotham City. Sendo assim, o Sr. Wayne optou por locar um veículo de forma a retornar com
urgência a cidade de Gotham. A locadora disponível era a DC Comics que possui dois modelos
de carros para alugar. O modelo morcego preto possui motor 1.0 aspirado, consome um litro
de gasolina a cada 16km e o aluguel era de $300. Já o modelo vampiro voador, possui motor 2.0
aspirado, consome um litro de gasolina a cada 11km e o valor do aluguel é de $500. A distância
entre Gotham City e Metrópolis é de 295Km. Essa distância foi percorrida pelo Sr. Wayne
utilizando um dos veículos da locadora DC. Sendo assim, desenvolva um programa que informe
quanto o Sr. Wayne gastou locando o veículo e viajando até Gotham City. Para a atividade,
considerar o preço da gasolina igual a $0,75.'''

#Para o modelo morcego
#A cada 16km consome 1 litro de gasolina
#O litro da gasolina está $0,75
print('-----------------------------------------------------------')
aluguel1 = 300
gasolina1= 295/16 #Aqui divide-se a distância total pelo total da distância que o carro faz com 1 litro,
#com isso será possível saber a quantidade de gasolina exata que utilizará
valor_gasolina1 = 0.75 * gasolina1
valor_total1 = aluguel1 + valor_gasolina1
print('Se o senhor wayne pegar o modelo morcego ele gastará: ${:.2f}'.format(valor_total1))
print('-----------------------------------------------------------')
#Para o modelo vampiro voador
#A cada 11km consome 1 litro de gasolina
#O litro da gasolina está $0,75
aluguel2 = 500
gasolina2 = 295/11 #Aqui divide-se a distância total pelo total da distância que o carro faz com 1 litro,
#com isso será possível saber a quantidade de gasolina exata que utilizará
valor_gasolina2 = 0.75 * gasolina2
valor_total2 = aluguel2 + valor_gasolina2
print('Se o senhor wayne pegar o modelo vampiro voador ele gastará: ${:.2f}'.format(valor_total2))
print('-----------------------------------------------------------')