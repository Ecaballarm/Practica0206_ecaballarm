# Escribir una función que reciba una muestra de números en una lista y devuelva su media.
def nums_lista(lista):
    '''Esta función hace la media de una lista de números'''
    longitud_lista = len(lista)
    sum_lista = sum(lista)
    media = sum_lista / longitud_lista
    return media


lista = []
usuario = input('Escriba una lista de números. Se mostrará la media: ')
lista = usuario.split(", ")
for i in range(len(lista)):
    lista[i] = int(lista[i])
print('La media es :', nums_lista(lista))





