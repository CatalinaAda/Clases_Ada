# Este programa es un juego de Trivia sobre programación en Python.
# Integrantes: 

#Modulo random (paso 4)
import random 
print('¡Te doy la bienvenida a la Trivia sobre Python!')
# Paso 3
# Nombre usuario
nombre = input('Ingresa tu nombre, por favor: ')
# Edad usuario
edad = int(input('Ingresa tu edad, por favor: '))

if edad >= 18:
    print(f' \n¡Hola {nombre}, Es hora de comenzar con la Trivia sobre python!\n ')
    print("\nAntes de comenzar, las instrucciones del juego son las siguientes: ")
    print('\ndebes de contestar correctamente las preguntas, por cada respuesta correcta \nvas a ganar 1 punto. Sin emabrgo, por cada respuesta incorrecta \nno sumaras puntos, pero si te equivocas más de tres veces pierdes el juego.')
    print('\n¡¡Ahora si, a jugar!')
else:
    print(f'Lo siento {nombre}, no tienes la edad mínima para jugar. ')
    exit()

# Paso 5 preguntas y respuestas
# Definir las preguntas y sus respuestas en un diccionario
preguntas = [
    ('Pregunta 1', 'verdadero'),               
    ('Pregunta 2', 'verdadero'),               
    ("Pregunta 3", 'falso'),
    ("Pregunta 4", "verdadero"),
    ("Pregunta 5", "Falso")
 ] # FALTA AÑADIR LAS PREGUNTAS!

# Usar shuffle para mezclar las preguntas 
random.shuffle(preguntas)

# Preguntar y evaluar la respuesta
score = 0
errores = 0

for pregunta, respuesta_correcta in preguntas:     #Cilco for para que me muestre las preguntas de manera aleatoria
    
    respuesta_usuario = input(f'{pregunta} (Responde Verdadero o Falso): ').lower()

    if respuesta_usuario == respuesta_correcta:
        print('Es correcto')
        score += 1
    else:
        print('Es incorrecto')
        errores += 1
        if errores >= 3:
            print(f'Tu puntuación es de {errores}',"\nJuego Terminado" )
            break

print(f'Puntuación final: {score}/{len(preguntas)}')