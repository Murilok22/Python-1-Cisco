hat_list = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no hat.
numbers_user = int(input("Numero que substituira o meio da lista:"))

hat_list[2] = numbers_user # Copiando o valor do quinto elemento para o segundo.
print("Conteúdo da lista anterior:", hat_list) # Imprimindo conteúdo da lista anterior.
del hat_list[-1]
print("Conteúdo da lista anterior:", hat_list) 
print ("Comprimento da nova lista:", len (hat_list))
print (hat_list) 
