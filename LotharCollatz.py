Co = int(input("Insira o número :"))  
tries = 0
i = 0
while Co != 1:
    tries += 1
    i = Co%2
    
    if i == 0:
      Co /= 2
      print(Co)
      
    if i == 1:
      Co = 3*Co+1
      print(Co)
      
print("tentativas: ", tries)