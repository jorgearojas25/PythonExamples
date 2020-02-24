# Escribir un programa que calcula el equivalente en grados Fahrenheit o Celsius de una
# temperatura t, el usuario debe indicar si la temperatura que ingreso esta en celcius o
# fahrenheit acompañando el valor por el carácter c o t respectivamente.
# Celsius / 5 = (Fahrenheit – 32) /9.


def temperature(temp, type):
    if type == 'c':
        return ("El equivalente en farenheit de " + str(temp) + " es " + str((temp*9/5)+32))
    if type == 'f':
        return ("El equivalente en celsius de " + str(temp) + " es " + str((temp-32)*(5/9)))
    elif type != 'c' or type != 'f':
        return ("tipo de medida no admitida")


print(temperature(float(input('Ingrese la temperatura: ')),input('Ingrese "c" si es celsius o "f" si es farenheit: ')))