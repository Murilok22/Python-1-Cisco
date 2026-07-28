# etapa 1
#i = "John Lennon"
#g = "Paul McCartney"
#f = "George Harrisony"
i = input("Digite o nome a ser inserido na lista: ")
beatles = []
print("Etapa 1:", beatles) 
beatles.append (i)
print("Etapa 2:", beatles)
for i in range(2):
    i = input("Digite o nome a ser inserido na lista: ")
    beatles.append(i)
print(beatles) 
print("Etapa 3:", beatles)
del beatles[-1]
del beatles[-1]
print("Etapa 4:", beatles)
beatles.insert(0, "Ringo Starr")

print("Etapa 5:", beatles)



# testando o tamanho da lista

("o fabuloso", len(beatles))

