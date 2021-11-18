print("Ingrese la operacion que desea realizar: ")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
operacion = int(input("Ingrese Operacion: "))
numero1 = input("Primer Numero: ")
numero2 = input("Segund Numero: ")


if operacion == 1:
    print("La suma es: ", (numero1 + numero2))
if operacion == 2:
    print("La resta es: ", (numero1 - numero2))
if operacion == 3:
    print("La multiplicacion es: ", (numero1 * numero2))
if operacion == 4:
    print("El coiciente es: ", (numero1 / numero2), "Y su resto es: ", (numero1 % numero2))