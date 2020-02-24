# Escribir un programa que calcule la suma de los cuadrados de los 100 primeros números
# enteros
import math

def squaring():
    result = 0
    for n in range(1, 101):
        result += math.pow(n,2)
    return result

print("Suma de cuadrados de  los primeros 100 numeros enteros: " + str(squaring()))