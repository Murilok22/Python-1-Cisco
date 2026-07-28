ano = int(input("Insira o ano: "))

if ano < 1582:
    print("Não dentro do período do calendário gregoriano")
elif ano%4==0:
    print("normal")
else:
    print("ano anormal! ", ano, "!")