hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))
minutofinal = (mins + dura) % 60
horafinal = hour + ((mins + dura) // 60)
print(horafinal,":", minutofinal)
# Escreva seu código aqui.

