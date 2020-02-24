import basicOperations
import validateBases


def leerNumero():
    return float(input('Ingrese un numero: '))

def leerValor():
    return input('Ingrese un valor: ')


if __name__ == "__main__":
    print('Uso de las funciones del modulo de operaciones basicas')
    print('La suma de los numeros ingresados es: ' +
          str(basicOperations.suma(leerNumero(), leerNumero())))

    print('La resta de los numeros ingresados es: ' +
          str(basicOperations.resta(leerNumero(), leerNumero())))

    print('La multiplicacion de los numeros ingresados es: ' +
          str(basicOperations.mult(leerNumero(), leerNumero())))

    print('La division de los numeros ingresados es: ' +
          str(basicOperations.div(leerNumero(), leerNumero())))

    print('La potencia de los numeros ingresados es: ' +
          str(basicOperations.potencia(leerNumero(), leerNumero())))
    print('Uso de las operaciones del modulo bases')
    print(str(validateBases.validarBinario(leerValor())))
    print(str(validateBases.validarOctal(leerValor())))
    print(str(validateBases.validarDecimal(leerValor())))
    print(str(validateBases.validarHexa(leerValor())))
