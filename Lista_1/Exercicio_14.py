'''14 - Um caçador de recompensas interestelar veio visitar o Brasil. Seu nome é Lobo um
motociclista do planeta Czarnia que buscava uma nova moto para sua coleção. Depois de muita
negociação o Lobo acabou encontrando a moto ideal e imediatamente fechou o negócio. Muito
feliz montou em sua moto e saiu pilotando para casa. Contudo, o Lobo não sabia que as
concessionárias brasileiras entregam o veículo praticamente sem combustível. Sendo assim,
parou no primeiro posto para abastecer, mas achou complicado sabe qual combustível seria
mais econômico utilizar: gasolina ou etanol? Você poderia ajudar? Informe qual combustível
será mais econômico.'''

# Função para verificar qual combustível é mais econômico
def combustivel_mais_economico(preco_gasolina, preco_etanol):
    if preco_etanol <= 0.7 * preco_gasolina:
        return "etanol"
    else:
        return "gasolina"

# Entrada dos preços
preco_gasolina = float(input("Informe o preço da gasolina: R$ "))
preco_etanol = float(input("Informe o preço do etanol: R$ "))

# Determinando o combustível mais econômico
resultado = combustivel_mais_economico(preco_gasolina, preco_etanol)

# Exibindo o resultado
print("O combustível mais econômico é: {}.").format(resultado)
