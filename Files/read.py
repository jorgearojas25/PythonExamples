# Escribir un programa que lea y muestre en pantalla el archivo generado en el ejercicio
# anterior


def leerTexto():
    f = open("D:/Academico/Universidad/ReposModelosII/PythonExamples/Files/file.txt",
             'r', encoding="utf-8")
    return f.read()



print(leerTexto())
