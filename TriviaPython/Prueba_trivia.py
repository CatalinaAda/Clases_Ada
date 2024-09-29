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
    print("Responde 'verdadero' o 'falso' según consideres correcta o incorrecta la afirmación.")
    
    # Lista de preguntas con respuestas correctas (True o False)
    preguntas = {
        "Python es un lenguaje de programación interpretado.": True,
        "HTML es un lenguaje de programación.": False,
        "El lenguaje C fue desarrollado antes que Python.": True,
        "JavaScript es lo mismo que Java.": False,
        "Git es un sistema de control de versiones distribuido.": True
    }

    # Convertir en tuplas y mezclar las preguntas
    lista_preguntas = list(preguntas.items())
    random.shuffle(lista_preguntas)

    # Inicializar el puntaje
    score = 0

    # Ciclo para mostrar y evaluar las respuestas
    for pregunta, respuesta_correcta in lista_preguntas:
        respuesta_usuario = input(f'{pregunta} (Responde "verdadero" o "falso"): ').lower()

        # Evaluación de la respuesta
        if (respuesta_usuario == 'verdadero' and respuesta_correcta) or (respuesta_usuario == 'falso' and not respuesta_correcta):
            print('¡Es correcto!')
            score += 1
        else:
            print('Es incorrecto')

        print(f'Tu puntuación actual es: {score}\n')

    # Resultado final
    print(f'Puntuación final: {score}/{len(lista_preguntas)}')

# Ejecutar el juego
if __name__ == "__main__":
    juego_trivia()
