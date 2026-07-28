numero = 777 
print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que escolhi. |
| Então, qual é o número secreto?   |
+===================================+
""")
# Leia o primeiro número. 
number = int(input("Digite um número ou digite 0 para parar: ")) 
  
# 0 termina a execução. 
while number != 0: 
    # Verifique se o número é ímpar. 
    if number == 777: 
        # Aumente o contador odd_numbers. 
        print("Muito bem, trouxa! Você está livre agora.", number," era o correto") 
    else: 
        # Aumente o contador even_numbers. 
        print("Ha ha! Você está preso no meu loop!")
    # Leia o número seguinte. 
    number = int(input("Digite um número ou digite 0 para parar: ")) 
