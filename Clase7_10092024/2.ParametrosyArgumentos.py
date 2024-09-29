# Definimos una función: parametros posicionales, con nombre y predeterminados

def presentar_persona(nombre, edad, ciudad="Desconocida", profesion="Desconocida"):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"Profesión: {profesion}")
    
    
# ejemplo de llamada a la función

#Usando argumentos posicionales

print("Ejemplo con argumentos posicionales: ")
presentar_persona("Ana", 30)

# Usando argumentos posicionales y con nombre
print("Ejemplo con argumentos posicionales y con nombre: ")
presentar_persona("Luis", 25, ciudad="Madrid", profesion="Ingreniero")

#Usando todos los argumentos pero con nombre

print("Ejemplo con de todos los argumentos con nombre: ")
presentar_persona(nombre="Marta", edad=34, ciudad="Madrid", profesion="Ingreniera")






