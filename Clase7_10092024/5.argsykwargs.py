# Ejemplo 1 - función que usa *args

def sumar_numeros(*args):
    
    total = 0
    
    for numero in args:
        total =+ numero
    return total
print("Ejemplo 1 - función que usa *args")
print(f"Suma de 1, 2, 3: {sumar_numeros(1,2,3)}")
print(f"Suma de 4, 5, 6, 7, 8: {sumar_numeros(4,5,6,7,8)}")

def mostrar_detalles(**kwargs):
    
    for clave, valor in kwargs.items():
        print(F"{clave}:{valor}")

print("Ejemplo 2 - funcion que usa *Kwargs: ")
mostrar_detalles(nombre="Ana", edad=30, ciudad="Madrid")


#Ejemplo 3 combinados 

def mostrar_info_completa(*args, **kwargs):
    print("Argumentos no nosmbrados: ")
    for arg in args:
        print(args)
    print("\nArgumentos nombrados:")
    for clave, valor in kwargs.items():
        print(F"{clave}:{valor}")
print("Ejemplos 3 comnbinados:")

mostrar_info_completa(1,2,3,nombre="Ana", edad=30, profesion="Ingeniera")


