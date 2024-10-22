'''
Dos pares de numeros que representen dos puntos en ele plano,
calcula y muestra la distancia entre ellos
Entradas:
  x1:int
  y1:int
  x2:int
  y2:int
Salidas:
  distancia  
'''
x1 = int(input("Ingrese elvalor de x1: "))
y1 = int(input("Ingrese el valor de y1: "))
x2 = int(input("Ingrese el valor de x2: "))
y2 = int(input("Ingrese el valor de y2: "))

distancia = ((x2- x2)*2 + (y2 - y1)*2) ** 0.5
print("La distancia entre los puntos es:", int (distancia))
