'''
  Programa que reciba una catidad de minutos y muestre en pantalla 
  a cuantas horas y minutos corresponde
Entadas:
    minutos: int
salida: 
    minutos y horas correspondientes
'''
minutos = input("ingresa los minutos")
minutos = int(minutos)
hora = minutos/60
minutos = minutos % 60
print("Las horas son : ",hora , minutos) 