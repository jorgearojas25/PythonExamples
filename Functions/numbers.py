# Escribir un programa, que con funciones, verifique si un carácter introducido es un número
# o no.

def evaluate(char):
    if char.isdigit():
        return "Es un numero"
    return"No es un numero"

print(evaluate(input('Ingrese una cadena para ver si es numero o no: ')))