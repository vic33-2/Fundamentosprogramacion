'''
calificaciom final de la materia 
entradas:
  cal1: int
  cal2: int
  cal:3 int
  examen final: int
  trabajo final: int
salida:
  promedio de parciales
  calificacion total
'''

cal1 = int(input("Ingresa la primera calificacion parcial: "))
cal2 =  int(input("Ingresa la segunda calififcacion parcial: "))
cal3 = int(input("Ingresa la tercera calificacion parcial: "))
examenfinal = int(input("Ingresa la calificacion del examen final: "))
trabajofinal = int(input("Ingresa la calificaccion del trabajo final: "))

promedio_parciales = (cal1 + cal2 + cal3) / 3
calificacion_total = (promedio_parciales) * 0.55 + (examenfinal * 0.30) + (trabajofinal * 0.15)

print("Tucalificacion final es:", int(calificacion_total))