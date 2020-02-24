# Crear un módulo que maneje funciones para operar en sistema octal, las operaciones que se
# deben implementar son suma, resta, multiplicación y división.

def validarOctal(number):
    for n in number:
        if int(n)>7 or int(n)<0:
            return "El numero no es operable en el sistema octal"
    return int(number)

print(str(validarOctal('89')))