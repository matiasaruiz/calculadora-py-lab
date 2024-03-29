#############
#  Imports  #
#############


import matesBasicas as doMath


################
#  Lazy stuff  #
################


def inAndProcess(ans):    
    aux = input("Primer Numero: ")
    if aux == "ans":
        return ans
    else:
        return aux

def doBasicOperations(ans):
    showBasicOperations()
    operator = input("Ingrese Operacion: ")
    
    num1 = inAndProcess(ans)
    num2 = inAndProcess(ans)

    ans = doMath.basicOperations(num1, num2,operator)
    showData(operator,ans)
    return ans


def doAnalisisOperations():
    showAnalisisOperations()
    #TODO: implement
    doMath.analisisOperations()

def doImaginaryOperations():
    showImaginaryOperations()
    #TODO: implement
    doMath.imaginaryOperations()

def doAlgebraicOperations():
    showIAlgebraOperations()
    #TODO: implement
    doMath.algebraicOperations()

###################
#  Graphic stuff  #
###################

def showMainMenu():
    print("+--------------------------------------------------+")
    print("|                    calcuTHON                     |")
    print("+--------------------------------------------------+")
    print("|                                                  +")
    print("| Ingrese el tipo de operacion que desea realizar: |")
    print("|   1. Basicas - (+ - * / mod)                     |")
    print("|   2. Analisis - (Proximamente)                   |") # (Lim, Derivada, Integral)
    print("|   3. Imaginarias - (Proximamente)                |")
    print("|   4. Algebraicas - (Proximamente)                |")
    print("|                                                  +")
    print("+--------------------------------------------------+")
    
def showBasicOperations():
    print("+--------------------------------------------------+")
    print("|                    calcuTHON                     |")
    print("+--------------------------------------------------+")
    print("|                                                  +")
    print("| Ingrese la operacion que desea realizar:         |")
    print("|   1. +                                           |")
    print("|   2. -                                           |") # (Lim, Derivada, Integral)
    print("|   3. *                                           |")
    print("|   4. /                                           |")
    print("|                                                  +")
    print("+--------------------------------------------------+")

def showAnalisisOperations():
    print("+--------------------------------------------------+")
    print("|                    calcuTHON                     |")
    print("+--------------------------------------------------+")
    print("|                                                  +")
    print("| Ingrese la operacion que desea realizar:         |")
    print("|   1. Limite                                      |")
    print("|   2. Derivada                                    |") # (Lim, Derivada, Integral)
    print("|   3. Integral                                    |")
    print("|                                                  +")
    print("+--------------------------------------------------+")

def showImaginaryOperations():
    print("+--------------------------------------------------+")
    print("|                    calcuTHON                     |")
    print("+--------------------------------------------------+")
    print("|                                                  +")
    print("| Ingrese la operacion que desea realizar:         |")
    print("|   1. ALGO                                        |")
    print("|   2. ALGO                                        |") # (Lim, Derivada, Integral)
    print("|   3. ALGO                                        |")
    print("|                                                  +")
    print("+--------------------------------------------------+")

def showIAlgebraOperations():
    print("+--------------------------------------------------+")
    print("|                    calcuTHON                     |")
    print("+--------------------------------------------------+")
    print("|                                                  +")
    print("| Ingrese la operacion que desea realizar:         |")
    print("|   1. ALGO                                        |")
    print("|   2. ALGO                                        |") # (Lim, Derivada, Integral)
    print("|   3. ALGO                                        |")
    print("|                                                  +")
    print("+--------------------------------------------------+")



def showData(operator,ans):
    if operator == "1":    
        print("+------------------------------------------------")
        print("| La suma es: ", ans, "                         |")
        print("+------------------------------------------------")
    if operator == "2":
        print("+------------------------------------------------")
        print("| La resta es: ", ans, "                         |")
        print("+------------------------------------------------")
    if operator == "3":
        print("+------------------------------------------------")
        print("| La multiplicacion es: ", ans, "                    |")
        print("+------------------------------------------------")
    if operator == "4":
        print("+------------------------------------------------")
        print("| El cociente es: ", ans, "                         |")
        print("+------------------------------------------------")
    if operator == "5":
        print("+------------------------------------------------")
        print("| El resto es: ", ans, "                          |")
        print("+------------------------------------------------")

