#programa para imprimir cuadrados de números y calcular la suma 

# Lista de números 

numeros = [1, 2, 3, 4, 5]

# Iniciamos variable

suma_cuadrados = 0

#Iterar sobre cada número en la lista

for numero in numeros:
    #Calcular el ciadrado del número
    cuadrado = numeros ** 2
    
    #imprimir el cuadrado
    print("El cuadrado del número: ", numeros, "Es:", cuadrado)
    
    suma_cuadrados += cuadrado
    
    #imprimir
print("La suma de los cuadrados es: ", suma_cuadrados)

