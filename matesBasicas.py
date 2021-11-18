def suma(num1, num2):
    return int(num1 + num2)
def resta(num1, num2):
    return int(num1 - num2)
def mul(num1, num2):
    return int(num1 * num2)
def div(num1, num2):
    return float(num1 / num2)
def mod(num1, num2):
    return int(num1 % num2)



def basicOperations(num1, num2, operator):
    num1 = int(num1)
    num2 = int(num2)

    if operator == "1":
        return suma(num1, num2)
    if operator == "2":
        return resta(num1,num2)
    if operator == "3":
        return mul(num1 * num2)
    if operator == "4":
        return div(num1, num2)
    if operator == "5": #operacion 5 es modulo
        return mod(num1, num2)

def analisisOperations():
    #TODO: implement
    return 0

def imaginaryOperations():
    #TODO: implement
    return 0

def algebraOperations():
    #TODO: implement
    return 0