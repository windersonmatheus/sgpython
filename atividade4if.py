municao = 1
distancia = 1000
posicao_descoberta = False

if municao > 0:
    if distancia > 999:
        if municao > 2:
            posicao_descoberta = True
            print("voce errou 2 vezes e foi descoberto")
            if  distancia > 1200:
                print ("voce errou todas e morreu")
            else:
                print ("voce errou duas vezes mas conseguiu acertar na terceira parabens")
        else:
            print("voce errou e morreu")
    else:
        print("voce acertou o alvo com 1 tiro")
else:
    print("soldado como voce consegue esquecer a municao como voce vai atirar sem municao")
