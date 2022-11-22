# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

nombre = input("Escribe tu nombre: ")
def saludo(nombre):
    """Función que muestra un saludo a el nombre que escibas"""
    print("¡Hola", nombre + "!")
    return

saludo(nombre)