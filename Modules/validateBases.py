# Crear un módulo que permita validar un número según la base en la cual este expresado, las
# bases validas deben ser 2, 8, 10 y 16.
import string


def validarOctal(number):
    for n in number:
        if int(n) > 7 or int(n) < 0:
            return "El numero " + number+" no es operable en el sistema octal "
    return int(number)


def validarBinario(number):
    for n in number:
        if int(n) > 1 or int(n) < 0:
            return "El numero " + number + " no es operable en el sistema binario "
    return int(number)


def validarDecimal(number):
    for n in number:
        if int(n) > 9 or int(n) < 0:
            return "El numero " + number + " no es operable en el sistema decimal "
    return int(number)


def validarHexa(number):
    if all(c in string.hexdigits for c in number):
        return number
    return "El numero " + number + " no es operable en el sistema hexadecimal "
    
