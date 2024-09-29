# Crear una tupla con varios valores

tupla_mixta = (1, "Hola", 3.5)

#Mostrar completa la tupla
print("Tupla completa ", tupla_mixta)

#Acceder a los elementos de la tupla por su índice (posición)

print("primer elemento de la tupla: ", tupla_mixta[0])
print("Segundo elemento de la tupla: ", tupla_mixta[1])
print("Tercero elemento de la tupla: ", tupla_mixta[2])

# Explicación tuplas inmutables

print("\nLas tuplas no se pueden modificar, Intentemos cambiar el primer elemento de la tupla: ")

# Ejemplo de intento de cambio que causaría error
# tupla_mixta[0] = 10

#Explicación clara de la inmutabilidad
print("Si intentamos hacer ¨tupla_mixta[0] = 10, Python mostrará por qué no se puede cambiar ningún elemento de una tupla.")

#Mostrar como sí podemos modificar una tupkla, creando una nueva tupla
tupla_mixta = (10, "Hola", 3.5)
print("nueva tupla con el primer elemento cambiado", tupla_mixta)
