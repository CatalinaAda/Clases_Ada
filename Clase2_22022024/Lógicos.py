# Operadores Lógicos and, or, not - Definimos distintas variables para usar en las comparaciones

a = 10
b = 5
c = 15
d = 8

# Operador AND
#Ambas condiciones deben ser verdaderas para que el resultado sea True

resultado_and = (a > b) and (c > d)
print(f"Resultado de and (a > B) and ( c > d): {resultado_and}")

# Operador OR
#Al menos una de las condiciones debe ser verdadera para que el resultado sea true

resultado_or = (a > b) or (c > d)
print(f"Resultado de or (a < b) or (c > d): {resultado_or}")

#Operador NOT
# El operador not invierte el valor de la expresión
# ( a < b es false porque 10 no es menor que 5  pero uso NOT cambia el valor por true

resultado_not = not(a < b)
print(f"Resultado de not (a < b): {resultado_not}")


# Combinación de los operadores lógicos AND OR y Not
resultado_combinado = (a > b) and (not (c < d)) or ( b > c)
print(f" Resultado combinado : {resultado_combinado}")
# (a > b) es true porque 10 > 5
# (c < d) es false porque 15 no es menor que 8, pero hay un not, entonces me lo convierte en true
# ( a > b) and ( c <d) es True porque True, and True
# (b > c) es True, entonces el True de arriba con el true del OR, son True por ende, nos da True