# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def num_cuadrado(num):
    """Función que calcula los cuadrados de una lista de números."""

    num_cuadrados = []
    for cuadrados in num:
        num_cuadrados.append(cuadrados**2)
    return num_cuadrados

print(num_cuadrado([6, 8, 12, 3, 7]))
