'''
Pide al ususario dos numeros y muestra la distancia entre ellos
Entradas:
   num1: int
   num2: int
Salidas:
   distancia    
'''
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

distancia = abs(num1 - num2)
print("La distancia entre los dos numeros es:", distancia)