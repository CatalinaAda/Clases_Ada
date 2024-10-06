
import random  # Importar el módulo random

numer_aleatorio = random.random()  # Generar un número aleatorio entre 0 y 1

# Imprimir el número aleatorio
print(f"Número Flotante aleatorio de 0 a 1: {numer_aleatorio}")

# Generar un número entero aleatorio entre 1 y 10

numer_entero = random.randint(1,10)
print(F"Número entero aleatorio entre 1 a 10: {numer_entero}")

#Seleccionar una fruta al azar de una lista

fruta = ["Manzana", "naranja", "Banana", "Uva", "Pera"]
fruta_elegida = random.choice(fruta)


print(F"La fruta elegida es : {fruta_elegida}")

#Mezclar aleatoriamente una lista de números 

numeros = [1,2,3,4,5]
random.shuffle(numeros)
print(f"Números mezclados: {numeros}")


#Generar un número flotante aleatorio entre 5,5 y 10,5

numer_aleatorio2 = random.uniform(5.5 , 10.5)  # Generar un número aleatorio entre 0 y 1

# Imprimir el número aleatorio
print(f"Número Flotante aleatorio entre 5.5 y 10.5: {numer_aleatorio2}")

#Seleccionar 3 letras al azar de una lista sin repetición

letras = ["a","b","c","d","e"]
seleccion_letras = random.sample(letras,3)

print(f"Letras seleccionadas: {seleccion_letras}")



