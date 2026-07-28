blocks = int(input("Insira o número de blocos:"))  
altura = 0
i = 1
while blocks >= i:
    blocks -= i
    print(i)
    i += 1
    altura += 1
print("A altura da pirâmide:", altura)

