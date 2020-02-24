# Modifique el ejercicio anterior para que el conteo se haga hacia atrás desde el tiempo leído
# hasta cero

from datetime import datetime, timedelta
import time

def leerNumero(nombre):
    return int(input('Ingrese un numero para ' + nombre + ': '))

def countdown(d=0, h=0, m=0, s=0):
    counter = timedelta(days=d, hours=h, minutes=m, seconds=s)
    while counter:
        time.sleep(1)
        counter -= timedelta(seconds=1)
        print("Time remaining: {}".format(counter))


countdown(leerNumero('dias'),leerNumero('horas'),leerNumero('minutos'),leerNumero('segundos'))