import matesBasicas as doMath
import facilities as makeItEasy

print("Ingrese la operacion que desea realizar: ")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

i= 1000
ans = 0

while i > 2:
    operacion = input("Ingrese Operacion: ")
    
    numero1 = makeItEasy.inAndProcess(ans)
    numero2 = makeItEasy.inAndProcess(ans)
    print(numero1, numero2)

    ans = doMath.operate(numero1, numero2,operacion)
    print(ans)

    if operacion == "1":    
        print("La suma es: ", ans)
    if operacion == "2":
        print("La resta es: ", ans)
    if operacion == "3":
        print("La multiplicacion es: ", ans)
    if operacion == "4":
        print("El coiciente es: ",ans,  "Y su resto es: ", (numero1 % numero2))
        