# Escribir un programa que compare dos cadenas de caracteres y nos diga si son idénticos o
# no.


def compararPalabras(palabra1, palabra2):
    indice = 0
    incorrecto = "Las palabras no son iguales"
    correcto = "Las palabras son iguales"
    if len(palabra1) != len(palabra2):
        return incorrecto
    while indice < len(palabra1):
        letraPalabra1 = palabra1[indice]
        letraPalabra2 = palabra2[indice]
        if letraPalabra1 != letraPalabra2:
            return incorrecto
        indice += 1
    return correcto


print(compararPalabras(input('Ingrese una palabra: '), input('Ingrese otra palabra: ')))
