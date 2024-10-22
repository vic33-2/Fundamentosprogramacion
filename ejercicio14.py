'''
Dado un numero de dos sifras, que permita 
obtener el numero invertido
Entradas:
  numero: int
Salidas:
  invertido:
'''
numero = int(input("Ingrese un numero de dos cifras: "))
if 10 <= numero <= 99:
    invertido = (numero % 10) * 10 + (numero // 10)
    print("El numero invertido es:", invertido)
else:
    print("Porfavor ingrese un numero de dos cifras.")    