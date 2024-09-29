# Definir una matriz de 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]  
    
]

# Acceder y mostrar algunos elementos específicos

print("Algunos elementos de la matriz: ")
print("Elemento en la fila 0 y columna 0: ", matriz[0][0])
print("Elemento en la fila 1 y columna 2: ", matriz[1][2])

print("\n Modificando elementos específicos: ")
matriz[0][1] = 10 #Cambiar elemento de la fila cero, columna 1
matriz[2][0] = 15 #Cambiar elemento de la fila 2, columna 0

print("Matriz después de las modificaciones: ", matriz)

print("\n Accediendo a una fila completa: ")
fila_completa = matriz[1] # Obtener toda la fila
print("Fila completa en la posición 1: ", fila_completa)

print("\n Reemplazando una fila completa; ")
matriz[1] = [20, 21, 22]
print("Matriz después de reemplazar la fila 1: ")
print(matriz)

# Trabajar con una submatriz (parte de una Matriz)

submatriz = [matriz[0][1:3], matriz[1][1:3]]
print("Submatriz extraida ", submatriz)

# Mostramos toda la matriz al final 

print("\nMatriz completa al final: ")
print(matriz[0])
print(matriz[1])
print(matriz[2])

