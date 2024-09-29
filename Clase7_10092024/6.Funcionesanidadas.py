# ejemplo 1 - básico funcion anidada

def funcion_externa(x):
    def funcion_interna(y):
        return y + 10
    return funcion_interna (x) #Llamada a la función interna con el valor x

#Llamada a la función externa 
resultado = funcion_externa(5)
print(f"Resultado de la función_externa(5): {resultado}")


#Ejemplo 2 - Closure

def crear_multiplicador(factor):
    def multiplicador(x):
        return x * factor
    return multiplicador