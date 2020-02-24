# Escribir un programa que calcula el IVA (16%) de un producto dado su valor de venta sin IVA.

def calcularIVA(number):
    return number*0.16

print('IVA: '+ str(calcularIVA(float(input('Precio del articulo: ')))))