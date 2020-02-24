# Escribir un programa que calcule la hipotenusa de un triángulo rectángulo
import math


def hypotenuse(cateto1, cateto2):
    return math.sqrt((math.pow(cateto1, 2)+math.pow(cateto2, 2)))


print('la hipotenusa es: ' + str(hypotenuse(float(input('Valor del cateto 1:')),
                                        float(input('Valor del cateto 2:')))))
