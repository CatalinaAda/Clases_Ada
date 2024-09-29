# Calcular el precio final con descuento
#Escribe un programa que calcule el precio final de un producto después de aplicar un descuento del 15% si el precio final es mayor a 200

valor_factura = float(input("Ingrese el valor de su factura: "))

if valor_factura > 200:
    precio_final = valor_factura - (valor_factura*0.15)
    print("El precio final de su factura sería, ", precio_final)
else:
    print("Su factura no tiene descuento")
    
    