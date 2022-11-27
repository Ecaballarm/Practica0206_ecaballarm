# Escribir una función que reciba un número entero positivo y devuelva su factorial.
# Realiza el ejercicio mediante bucles interactivos y mediante una función recursiva.
def factorial(num):
   '''Esta función hace el factorial del numero que introduzcas'''
   if num == 0:
       return 1
   else:
     return num * factorial(num-1)
numero = int(input('Introduzca un número: '))
print('El factorial del número introducido es: ', factorial(numero))