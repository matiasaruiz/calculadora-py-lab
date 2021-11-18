import matesBasicas as doMath
import facilities as makeItEasy
import sys


makeItEasy.desplegarMenuPrincipal()
tipo =input("Ingrese el tipo de operacion: ")

i= 1000
ans = 0


if tipo == "1":
    while i > 2:
       ans = makeItEasy.doBasicOperations(ans)
if tipo == "2":
    while i > 2:
        makeItEasy.doAnalisisOperations()
if tipo == "3":
    while i > 2:
        makeItEasy.doImaginaryOperations()
if tipo == "4":
    while i > 2:
        makeItEasy.doAlgebraicOperations()
if tipo == "5":
    print("chau xd")
    sys.exit(0)



        