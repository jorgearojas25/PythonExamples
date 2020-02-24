# Escribir un programa que mediante funciones recursivas calcule el termino “x” de la serie de
# fibonacci.


def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


print("El numero de la seri es: " +
      str(Fibonacci(int(input('Ingrese la posicion que desesa conocer de la serie de Fibonnaci: ')))))
