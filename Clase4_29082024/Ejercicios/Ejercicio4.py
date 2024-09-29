# Ejercicio 4: Manipulación de Tuplas y Comprobación de Índices
# • Crea una tupla llamada frutas con los siguientes elementos:
# ("manzana", "banana", "cereza").
# • Usa el método index para encontrar la posición de la fruta "banana".
# • Verifica si la fruta "naranja" está en la tupla. Si no está, muestra un
# mensaje indicando que no está presente.

frutas = ("manzana", "banana", "cereza")

posicion_fruta = frutas.index("banana")

print("La posición de Banana es: ", posicion_fruta)


print("\n  ")

valor_buscado = "Naranja"

if valor_buscado in frutas:
    
    print("La fruta buscada sí está en la lista")
else:
    print("La fruta buscada no está en la lista")

