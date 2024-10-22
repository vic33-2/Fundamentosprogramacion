'''
Una tienda ofrece descuento del 15% sobre el total de la compra 
y un cliente desea saber cuamto debera de paagar finalmente
'''
def cacular_total_pago(total_compra):
    descuento = total_compra * 0.15
    total_a_pagar = total_compra - descuento
    return total_a_pagar

total_compra = int(input("introduce el total de compra: "))
total_a_pagar = cacular_total_pago(total_compra)
print(f"total a pagar despues del descuento: {total_a_pagar}")