# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
def area_circulo(radio):
    area = 3.1415*radio*radio
    return area

def volumen_cil(altura,area):
    vol = area*altura
    return vol

radio = float(input("Introduce el radio del circulo: "))
altura = float(input("Introduce la altura: "))
area = area_circulo(radio)
volumen = volumen_cil(altura, area)
print("El area del circulo es: ", area)
print("El volumen del cilindro es: ", volumen)


