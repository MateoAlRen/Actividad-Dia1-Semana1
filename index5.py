print("Adivina el numero del 1 al 10")

numero = int(input("ingrese el numero:  "))

if numero>8:
    print("Tu numero es mayor que el correcto")
elif numero<8:
    print("Tu numero es menor que el correcto")

if numero ==8:
    print("Adivinaste!")