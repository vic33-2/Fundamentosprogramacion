'''
programa 2:
    Crear un programa que calcule area y perimetro
    de un triangulo
Entradas:
    base: integer
    altura: integer 
Salidas:
    area: integer
    perimetro: integer
'''
base = input('Ingrese la base: ')
base = int(base)
altura = input('Ingresa la altura: ')
altura = int(altura)
area = base * altura 
perimetro = (base + altura) * 2 
print ("El area del rectangulo es: ", area)
print ("El perimetro de el rectangulo es: ",perimetro)