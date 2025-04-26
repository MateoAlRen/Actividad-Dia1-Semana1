print("Clasificación de IMC")

imc = float(input("Ingrese su peso:  "))
alt = float(input("Ingrese su altura:  "))
alt2 = alt*2
imc2 = imc / alt2

if imc2 < 18.5:
    print("Usted tiene bajo peso")
elif 18.5 < imc2 and imc2 < 24.9:
    print("Usted tiene peso normal")
if 25 < imc2 and imc2 < 29.9:
    print("Usted tiene sobrepeso")
elif 30 < imc2:
    print("Usted tiene obesidad")

    print(imc2)