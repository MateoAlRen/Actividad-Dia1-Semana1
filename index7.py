print("Balanza de numeros")

Numero1 = int(input("Escoge un numero:  "))
Numero2 = int(input("Escoge otro numero:  "))

if Numero1 == Numero2:
    print("Tus numeros son iguales")
elif Numero1 < Numero2:
    print(Numero2, "Es mayor que", Numero1)

if Numero1 > Numero2:
    print(Numero1, "Es mayor que", Numero2)