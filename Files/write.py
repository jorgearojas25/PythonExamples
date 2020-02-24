# Escribir un programa que escriba la lista de caracteres ASCII dentro de un archivo de texto


def escribirTexto():
    texto = ""
    for n in range(1, 254):
        texto += " " + chr(n)
    with open("D:/Academico/Universidad/ReposModelosII/PythonExamples/Files/file.txt", 'w', encoding="utf-8") as f:
        f.write(texto)
    return texto


print(escribirTexto())
