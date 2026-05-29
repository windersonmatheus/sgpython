import random
numeroMaximo = int(input("vamos adivinhar de 1 ate que numero? "))
chances = int(input("quantas chances voce tem? "))
numerodesconhecido = 0
numerocerto = random.randint(1,numeroMaximo)
while numerocerto != numerodesconhecido and chances > 0 :
    numerodesconhecido = int(input("digite um numero: "))
    if numerocerto > numerodesconhecido:
        print ("o correto e maior")
        chances -= 1
    elif numerocerto < numerodesconhecido:
        print ("o correto e menor")
        chances -= 1
    else :
        print ("na lata campeao")

if chances == 0 and numerocerto != numerodesconhecido:
    print ("poxa amigo nao foi dessa vez,acabaram suas chances")
