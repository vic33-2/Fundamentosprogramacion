'''
Realiza un algoritmo que lea un mumero y muestre su
raiz cuadrada y su raiz cubica
Entradas;
 numero: int
Salidas:
 raiz cuadrada:
 raiz cubica:
'''
numero = int(input("Ingrese el numero: "))

raiz_cuadrada = numero ** 0.5
raiz_cubica = numero ** (1/3)

print("La raiz cuadrada es:", int(raiz_cuadrada))
print("La raiz cubica es:", int(raiz_cubica))