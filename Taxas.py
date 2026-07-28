income = float(input("Entre com os rendimentos anuais "))

if income < 85528:
 tax = income * 0.18 - 556.02

if income >= 85528:
 tax = income * 0.32 + 14839.02

if  tax < 0:
    tax = 0 
    
tax = round(tax, 0)
print("A taxa é:", tax, "thalers") 
 