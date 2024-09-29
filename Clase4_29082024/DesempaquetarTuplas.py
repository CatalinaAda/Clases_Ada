# Ejemplo 1: Desempaqietado básico de tuplas

# Crear una tupla con varios tipos de datos

mi_tupla = 1, "Python", 3.14

# Desempaquetar la tupla

numero, lenguaje, pi = mi_tupla
#Mostrar el valor de cada variable después del desempaquetado
print("Número: ", numero)
print("Lenguaje: ", lenguaje)
print("Pi: ", pi)

#ejemplo 2: Número de variables no coincide con el número de elementos

#Crear una tupla con 3 elementos
mi_tupla = 1, "python", 3.14
#Intentar desempaquetar en dos variables (esto causará error)
#numero, lenguaje, = mi_tupla


#Ejemplo  3: Desempaquetado con el operador *
#Crear una tupa con varios elemetos
mi_tupla = (1, "python", 3.14, "tuplas", "Desempaquetado")
# desempaquetar la tulpla con el operador *
primer_elemeto, *resto = mi_tupla
#Mostrar los resultados

print("\n primer elemento: ", primer_elemeto)
print("resto de los elementos: ", resto)
