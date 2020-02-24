# Decir si una frase es o no un palíndromo, es decir, si se lee igual de derecha a a izquierda
# que de izquierda a derecha.

igual, aux = 0, 0
texto = input("Ingrese la palabra que desea evaluar: ")
for ind in reversed(range(0, len(texto))):
    if texto[ind].lower() == texto[aux].lower():
        igual += 1
    aux += 1
if len(texto) == igual:
    print("El texto es palindromo!")
else:
    print("El texto no es palindromo!")
