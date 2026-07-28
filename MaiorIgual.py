number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

largest_number = number1

if number3/largest_number>=1:
    largest_number = number3
if number2/largest_number>=1:
    largest_number = number2

print("O maior número é:", largest_number) 
