nota1 = int(input("digite sua nota1: "))
nota2 = int(input("digite sua nota2: "))
nota3 = int(input("digite sua nota3: "))
media =(nota1 + nota2 + nota3) /3
if media < 5:
    print("nota abaixo do necessario reprovado")
elif media ==10:
    print("muito bem voce tirou uma nota perfeita")
else:
    print("otima nota aprovado")
