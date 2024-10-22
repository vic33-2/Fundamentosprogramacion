'''
Intercabie los valores de ambas variables y muestre 
cuanto valen al final las dos varibles 
Entradas:
   A: int
   B: int
Salidas:
intercambi de valores   
'''
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))

# Intercambio de valores 
A,B = B, A

print("El valor de A ahora es:", A)
print("El valor de B ahora es:", B)