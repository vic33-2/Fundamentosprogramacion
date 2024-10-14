'''
Ejerciccio 3:
    Programa que calcula la hipotenusa de un triangulo
    rectangulo a partir de sus catetos 
Entradas:
    cateto1: int
    cateto2: int
Salidas:
    hipotenuza
Analisis
    Se resuelve con el teorema de pitagoras
'''
import math
cateto1 = input("Escribe el cateto 1: ")
cateto1 = int(cateto1)
cateto2 = int(input('escribe el catto 2'))
hipotenuza = cateto1 * cateto1 + cateto2 * cateto2
hipotenuza = hipotenuza ** (1/2)
hipotenuza = math.sqrt (hipotenuza)
print(' la hipotenusa es: ', hipotenuza)