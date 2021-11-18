def operate(numero1, numero2, operacion):
    numero1 = int(numero1)
    numero2 = int(numero2)

    if operacion == "1":
        return numero1 + numero2
    if operacion == "2":
        return numero1 - numero2
    if operacion == "3":
        return (numero1 * numero2)
    if operacion == "4":
        return numero1 / numero2