'''
'''
def calcular_total_vendedor(sueldo_base, ventas):
    comisiones = sum(ventas) * 0.10
    total_recibido = sueldo_base + comisiones 
    return comisiones, total_recibido

sueldo_base = 1000
ventas = []
ventas.append(int(input("venta total: ")))
ventas.append(int(input("venta total: ")))
ventas.append(int(input("venta total: ")))
comisiones, total_recibido = calcular_total_vendedor(sueldo_base, ventas)
print(f"comisiones: {comisiones}")
print(f"total recibido en el mes: {total_recibido}")
