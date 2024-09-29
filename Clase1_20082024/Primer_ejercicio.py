# 1. Declaración de Variables y Constantes
edad = 33           #número
nombre = "Catalina"      # Cadena de texto (string)
esta_estudiando = True  #Booleano

# Declaración de Constante
PI = 3.14           #Número
PAIS = "Colombia"   #Cadena de texto(string)

# 2. Leer valores por Teclado
edad = int(input("Introduce tu edad: "))
nombre = input("Introduce tu nombre: ")   
esta_estudiando = input("¿Estás estudiando? (Sí/no): ").lower() =="Sí"  

# 3. Tipos de datos
cantidad_de_libros = 10          #número (int)
titulo_libro = "El Principito"   # Cadena de texto (String)
es_interesante = True           #Booleano (bool)
temas = ["Aventura", "Fantasía", "Filosofía"]       #Lista (array)
autor = {                                           #diccionario
    "nombre": "Antoine de Saint-Exupéry",
    "nacionalidad": "Francesa"
}
# convertir tipos de datos
edad_str = str(edad)        #Convierte número a cadena de texto
cantidad_de_libros_float = float(cantidad_de_libros)   #Convertir entero a número de punto flotante

# 4. Imprimir resultados en la consola

print("Nombre: ", nombre)
print("Edad", edad)
print("¿Está estudiando?", esta_estudiando)
print("Constante de PI: ", PI)
print("Constante de País: ", PAIS)
print("Cantidad de libros: ", cantidad_de_libros)
print("Título del libro: ", titulo_libro)
print("¿Es interesante?: ",es_interesante)
print("Temas del libro", temas)
print("Autor del Libro: ", autor)
print("Edad (como cadena de texto): ", edad_str)
print("Cantidad de libros (Como float): ", cantidad_de_libros_float)

