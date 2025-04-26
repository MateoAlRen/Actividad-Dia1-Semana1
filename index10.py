print("Numeros Rango")

numero = int(input("Dame un numero cualquiera:  "))

if numero < 0 and numero > 10:
    print("El numero no está en el rango")
elif numero > 0 and numero < 10:
    print("El numero está en el rango")