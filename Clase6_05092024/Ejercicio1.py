# Ejercicio 1

lista_numeros = {1, 2, 3, 4, 5, 7, 7, 8, 4, 9, 8, 23, 44, 44, 2}

#Crear set para eliminar los duplicados

print(f'Esta es mi lista sin eliminar duplicados: {lista_numeros}')

lista_set = set(lista_numeros)

print(f'Esta es mi lista cuando se eliminaron duplicados: {lista_set}')

# Contar cuántos números son mayores que X número y almacenarlos en un nuevo set

mayores = 5

numeros_mayores = set()

for numero in lista_numeros:
    if numero > mayores:
        numeros_mayores.add(numero)
        
print(f" Mi nuevo conjunto de números mayores que el 5 es: {numeros_mayores}")
        
    