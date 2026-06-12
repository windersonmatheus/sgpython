NomeDosAlunos = ["davi", "gabriel", "joao","winderson"]
print ("este programa e uma lista que tem o nome dos alunos e professor em ordem alfabetica e a funcao dele e achar seu nome pelo indice")
print ("os seguites nonms estao na lista")
print (NomeDosAlunos)
indiceDoAluno = int(input("me de o numero do aluno: "))
if indiceDoAluno >= len(NomeDosAlunos):
    print ("o numero mencionado por voce e maior que o tamanho da lista")
elif indiceDoAluno < 0:
    print ("o numero mencionadon por voce e menor que o tamanho da lista")
else:
    print (NomeDosAlunos[indiceDoAluno])
