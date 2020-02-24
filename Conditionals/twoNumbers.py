# Escribir un programa que lea dos números desde el teclado y si el primero es mayor que el
# segundo intercambie sus valores.


def evaluateNumbers(number1, number2):
    if number1 > number2:
        return str(str(number2) + " " + str(number1))
    return str(str(number1) + " " + str(number2))


print('el orden resulante es ' + str(evaluateNumbers(float(input('Ingrese numero: ')),
                                                     float(input('Ingrese otro numero: ')))))
