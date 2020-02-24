# Escribir un programa que solicite cinco números, los almacene en una lista y luego calcule
# la media aritmética de esos números. 

def crearLista():
    lista = []
    n = 1
    while len(lista) < 5:
        lista.append(float(input('Ingrese un numero: ')))
        n += 1
    return lista

def promedioLista(lista):
    suma = 0
    for n in lista:
        suma += n
    return suma/len(lista)

print('el promedio de la lista es: ' + str(promedioLista(crearLista())))
        
    