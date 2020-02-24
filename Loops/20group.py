# Escribir un programa que escriba los números comprendidos entre 1 y 1000. El programa
# escribirá en la pantalla los números en grupos de 20, solicitando al usuario si quiere o no
# continuar visualizando el siguiente grupo de números.


def group(count):
    lista = []
    base = (count*20+1) - 20
    for n in range(base, count*20+1):
        lista.append(n)
    return lista


def showNumbers():
    count = 1
    while input('para detenerse marque n: ') != 'n':
        if count > 50:
            return False
        print(group(count))
        count += 1


showNumbers()
