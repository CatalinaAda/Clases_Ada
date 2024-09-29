# Juego de Trivia en Python con preguntas True o False
import random

# Función principal del juego
def juego_trivia():
    # Bienvenida y datos del jugador
    print("¡Bienvenido al Juego de Trivia!")
    nombre = input("Por favor, ingresa tu nombre: ")
    edad = int(input("¿Cuál es tu edad? "))

    # Verificación de la edad mínima
    if edad < 18:
        print("Lo siento, debes tener al menos 18 años para jugar.")
        return

    print(f"Hola {nombre}, ¡prepárate para la trivia sobre programación!")
    print("Responde 'True' o 'False' según consideres correcta o incorrecta la afirmación.")
    
    # Lista de preguntas con respuestas correctas (True o False)
   # Paso 5 preguntas y respuestas
# Paso 5 preguntas y respuestas
# Definir las preguntas y sus respuestas en un diccionario
preguntas = {
    'Pregunta 1': 'verdadero',               
    'Pregunta 2': 'verdadero',               
    "Pregunta 3": 'falso'
 } # FALTA AÑADIR LAS PREGUNTAS!

# Convertir en tuplas
Lista_preguntas = list(preguntas.items())

# Usar shuffle para mezclar las preguntas 
random.shuffle(Lista_preguntas)

# Preguntar y evaluar la respuesta
score = 0

for preguntaX, respuesta_correcta in Lista_preguntas:     #Cilco for para que me muestre las preguntas de manera aleatoria
    respuesta_usuario = input(f'{preguntaX} (Responde verdadero o falso): ').lower()

    if (respuesta_usuario == 'verdadero' and respuesta_correcta) or (respuesta_usuario == 'falso' and not respuesta_correcta):
        print('Es correcto')
        score += 1
    else:
        print('Es incorrecto')
    print(f'Tu puntuación es de {score}')

print(f'Puntuación final: {score}/{len(Lista_preguntas)}')

