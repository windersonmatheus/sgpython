preco = 10
print("vendedor: o hamburguer ta 10 reais")
quantidade = 5
print("cliente: Eu quero 5 hamburgueres")
carteira = 750
print("cliente: Eu tenho " + str(carteira) + " reais")
if carteira < preco:
    print("vendedor: senhor esta faltando " + str(preco*quantidade-carteira) + " reais")
if carteira > preco:
    print  ("vendedor: esta tudo certo senhor sobrou " + str(carteira-preco*quantidade) + " reais agora e so esperar")
 
