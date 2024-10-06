# Instrucciones: Solicita al usuario que ingrese un número decimal.
#Usa las siguientes funciones del módulo math para realizar diferentes cálculos:

#math.ceil(): Redondear al entero superior.

#math.floor(): Redondear al entero inferior.

#math.sqrt(): Obtener la raíz cuadrada.

#math.factorial(): Calcular el factorial (solo si es un número entero no negativo).

#math.pow(): Elevar el número a la potencia de otro número.

import math

numero = float(input("Ingrese un número: "))

numero_redondeado = math.ceil(numero)
print(f"Este es el valor redondeado: {numero_redondeado}")

numero_redondeado_abajo = math.floor(numero)
print(f"Este es el valor redondeado hacia abajo: {numero_redondeado_abajo}")

numero_raiz = math.sqrt(numero)
print(f"Este es el valor de la raíz: {numero_raiz}")


numero_factorial = math.factorial(numero_redondeado)
print(f"Este es el valor factorial de {numero} es: {numero_redondeado}")

numero_pow = math.pow(numero,3)
print(f"Este es el valor elevado a la potencia de 3 es: {numero_pow}")