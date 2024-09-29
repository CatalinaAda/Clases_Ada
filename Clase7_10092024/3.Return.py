#Ejemplo básico de return

def calcular_cuadrado (numero):
    return numero*numero

resultado = calcular_cuadrado(4)

print("Ejemplo básico de return: ")
print(f"El cuadrado de 4 es {resultado}: ")


# Ejemplo 2 - Retorno de multiples valores
def obtener_datos():
    nombre = "Ana",
    edad = 30,
    return nombre, edad    # Retorne los valores como una tupla

# Asignamos los valores a una variable 

## nombre, edad = obtener_datos

##print("ejemplo 2 - retonor de multiples valores: ")
##print(f"Nombre: {nombre}, Edad: {edad}")
##print()

# Ejemplo 3 - sin return

def clasificar_numero(numero):
    if numero > 0:
        return "Positivo"
    elif numero <0:
        return "Negativo"
    else:
        return "Cero"
    
resultado1 = clasificar_numero(10)
resultado2 = clasificar_numero(-5)
resultado3 = clasificar_numero(0)



print("Ejemplo 3 - sin return:")
print(f"El número 10 es: {resultado1}")
print(f"El número -5 es: {resultado2}")
print(f"El número 0 es: {resultado3}")

# Ejemplo 4: Sin return

def mostrar_mensaje():
    print("Esta función no retorna valo.r")

resultado = mostrar_mensaje()

print("Ejemplo 4: sin return")
print(f"Valor retornado {resultado}")







