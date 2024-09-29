# Programa para adivinar un número secreto

# Definimos el número secreto

numero_secreto = 7

# inicializar la variable para almacenar el número del usuario

numero_adivinado = None

print("Adivina el número secreto, entre el 1 y el 10: ")

# Bucle While que continua hasta que el usuario adivine el número secreto

while numero_adivinado != numero_secreto:
    #Solicitar al usuario ingresar un número
    numero_adivinado = int(input("Introduce tu número acá:"))
    #Comprobar si el número adivinado es correcto
    if numero_adivinado < numero_secreto:
        print("Demasiado bajo, intenta de nuevo")
    elif numero_adivinado > numero_secreto:
        print("Demasiado alto, intenta de nuevo")
    else:
        print("Correcto, acertaste, es el número: ", numero_adivinado)
        
print("Gracias por jugar")

