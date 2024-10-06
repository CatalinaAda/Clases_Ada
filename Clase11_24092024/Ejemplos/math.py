import math

# Ejemplo con constantes 

print(f"El Valor de PI es: {math.pi}")
print(f"El Valor de e es: {math.e}")

# Calcular el seño de 90 grados

angulo_grados = 90
angulo_radianes = math.radians(angulo_grados)

print(f"Seno de {angulo_grados} grados es: {math.sin(angulo_radianes)}")

#Calcular Logarítmos 

numero = 100

print(f"Logarítmo natural de {numero} es: {math.log(numero)}")
print(f"Logarítmo en base 10 del {numero} es: {math.log10(numero)}")

#Redondeo
numero2 = 4.67

print(f"{numero2} redondeo hacia abajo es: {math.floor(numero2)}")
print(f"{numero2} redondeo hacia arriba es: {math.ceil(numero2)}")

#Raiz cuadrada

num = 16

print(f"La raíz cuadrada de {num} es: {math.sqrt(num)}")




