numerodesconhecido = 0
numerocerto = 5
while numerocerto != numerodesconhecido:
    numerodesconhecido = int(input("digite um numero: "))
    if numerocerto > numerodesconhecido:
        print ("o correto e maior")
    elif numerocerto < numerodesconhecido:
        print ("o correto e menor")
    else :
        print ("na lata campeao")
