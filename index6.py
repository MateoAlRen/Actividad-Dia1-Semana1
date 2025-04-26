print("Hora de pagar la cuenta")

cuenta = int(input("Ingrese la cuenta:  "))
propina = int(input("Ingrese la propina:  "))


if propina == 20:
   print("Su propina es", cuenta/100 * 20)
elif propina == 15:
   print("Su propina es", cuenta/100 * 15)

if propina == 10 :
   print("Su propina es", cuenta/100 * 10)

