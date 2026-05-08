idade = int(input("digite sua idade: "))
ingresso =input("digite sim se voce tem ingresso: ")
vip = input("digite sim se voce tem VIP: ")
autorizacao_dos_pais = input("digite sim se voce tem autorizacao dos pais: ")
if idade < 12:
    print("voce eh muito novo acesso negado")
elif idade >= 18 and (ingresso == "sim" or vip == "sim" ):
    print("esta tudo certo pode entrar")
elif idade < 18  and autorizacao_dos_pais =="sim"and (ingresso == "sim"or vip == "sim"):
    print("tudo beleza pode entrar")
else:
    print("infelizmente seu acesso foi negado")
