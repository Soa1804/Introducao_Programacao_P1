'''5 – Para uma eleição ser considerada válida é necessário que a soma dos votos de todos os
candidatos seja superior a soma dos votos brancos e nulos. Na aldeia da folha, foi realizada a
eleição do sexto Hokage. Nela os candidatos foram: Naruto Uzumaki, Sakura Haruno e Shin
Aburame. Faça um programa que informe o vencedor da eleição se a mesma for considerada
válida.'''

#Primeiro tem que pedir ao usúario para informar todos os votos
naruto_uzumaki = int(input('Informe quantos votos o candidato Naruto Uzumaki teve: '))
sakura_haruno = int(input('Informe quantos votos o candidato Sakura Haruno teve: '))
shin_aburame = int(input('Informe quantos votos o candidato Shin Aburame teve: '))
votos_brancos = int(input('Digite os votos brancos: '))
votos_nulos = int(input('Digite os votos nulos: '))

total_votos = naruto_uzumaki + sakura_haruno + shin_aburame + votos_brancos + votos_nulos
concorrentes_naruto = sakura_haruno+shin_aburame+votos_brancos+votos_nulos
concorrentes_sakura = naruto_uzumaki+shin_aburame+votos_brancos+votos_nulos
concorrentes_shin = naruto_uzumaki+sakura_haruno+votos_brancos+votos_nulos

if naruto_uzumaki > concorrentes_naruto:
    print('O vencedor foi Naruto Uzumaki com {} votos'.format(naruto_uzumaki))

elif sakura_haruno > concorrentes_sakura:
    print('A vencedora foi Sakura Haruno com {} votos'.format(sakura_haruno))
    
else:
    print('O vencedor foi Shin Aburame com {} votos'.format(shin_aburame))

print('O total de votos na Aldeia da Folha foi {}'.format(total_votos))