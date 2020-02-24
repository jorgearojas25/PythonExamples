# Escribir una función recursiva que halle la suma de los primeros "n" números naturales.

def sumarNumeros(number):
    if number==0:
        return number
    return number + sumarNumeros(number-1)

print(sumarNumeros(int(input('La suma de los numeros naturales hasta: '))))