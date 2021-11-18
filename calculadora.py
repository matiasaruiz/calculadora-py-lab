import matesBasicas as doMath

print("Ingrese la operacion que desea realizar: ")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

i= 1000

while i > 2:
    operacion = input("Ingrese Operacion: ")
    
    aux1 = input("Primer Numero: ")
    if aux1 == "ans":
        numero1 = ans
    else:
        numero1 = int(aux1)

    aux2 = input("Segundo Numero: ")
    if aux2 == "ans":
        numero2 = ans
    else:
        numero2 = int(aux2)

    ans = doMath.operate(numero1, numero2,operacion)
    
    if operacion == "1":    
        print("La suma es: ", ans)
    if operacion == "2":
        print("La resta es: ", ans)
    if operacion == "3":
        print("La multiplicacion es: ", ans)
    if operacion == "4":
        print("El coiciente es: ",ans,  "Y su resto es: ", (numero1 % numero2))
        