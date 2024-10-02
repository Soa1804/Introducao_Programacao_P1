'''A potência de um raio é alta, mas a energia que ele transfere para a
terra é relativamente pequena:
• A intensidade de um raio é de cerca de 30 mil Ampères, o que é mil vezes
maior que a intensidade de um chuveiro elétrico.
• A voltagem de um raio pode variar entre 100 milhões e 1 bilhão de Volts.
• A energia elétrica total de um relâmpago é de cerca de 300 kWh.

• A energia que um raio transfere da nuvem para a terra é de cerca de 500
quilowatts, o que é pouco mais do que o consumo mensal de uma casa.

Essa foi a informação que o professor Emmett Brown utilizou para ligar o
DeLorean DMC-12 a um para-raios levando a energia coletada para o
capacitador de fluxo. Como sabemos, um capacitor é um componente
eletrônico que armazena cargas elétricas temporariamente, liberando-as
quando necessário. Ele perde sua carga lentamente e necessita de nova
alimentação para atingir seu máximo potencial. No caso do capacitor do
DeLorean a carga máxima era de 800Volts. E a viagem no tempo só poderia
acontecer se o capacitor de fluxo estivesse em seu potencial máximo (800).
Sendo assim, elabore um sistema que gere um valor aleatório entre 100 e 1000
representando a potência do raio e informe se a viagem no tempo ocorreu.'''
import random
capacidade_absorvida = int(random.randint(100,1000))

if capacidade_absorvida >= 800:
    print('A viagem no tempo foi um sucesso, a energia foi de {}'.format(capacidade_absorvida))

else:
    print('A viagem no tempo foi impossível por falta de energia, a energia foi de {}'.format(capacidade_absorvida))