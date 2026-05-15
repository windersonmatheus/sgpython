idade = int(input("digite sua idade: "))
experiencia = input("digite se voce tem experiencia: ")
antecedentes = input("fale se voce tem antecedentes: ")
ESC = input("voce tem ensino superior completo: ")
indicacao = input("voce teve uma indicacao: ")
if idade >= 18 and experiencia=="sim" or ESC=="sim" and antecedentes=="nao":
    print("tudo voce tem a idade e tem experiencia nescessaria e nao tem antecedentes esta contrado")
elif  (ESC=="sim" or indicacao=="sim") and experiencia=="nao" and antecedentes=="nao":
    print("voce chamou nossa atencao compareca na entrevista")
else:
    print("sem palavras")
