# Escriba un programa que calcule el máximo y el mínimo de dos números usando funciones.
# Con tal fin, proceda como sigue:
# • Escriba un procedimiento Leer que lea un número.
# • Escriba una función que dados dos números, devuelva el máximo de ellos.
# • Escriba una función que dados dos números, devuelva el mínimo de ellos.
# • Escriba el programa principal que lea dos números, obtenga el mayor y el menor de
# ellos, y muestre el resultado en pantalla.

def leerNumero():
    return float(input('Ingrese un numero: '))

def numeroMayor(numero1, numero2):
    if numero1 > numero2:
        return numero1
    return numero2

def numeroMenor( numero1, numero2):
    if numero1>numero2:
        return numero2
    return numero1

if __name__ == "__main__":
    valor1 = leerNumero()
    valor2 = leerNumero()
    print("El numero mayor es: " + str(numeroMayor(valor1, valor2)))
    print("El numero menor es: " + str(numeroMenor(valor1, valor2)))

