# Scope: Alcance local y global en python

# declarar una variable global

x = 20

def funcion_local():
    x = 10   #En este caso X es una variable local 
    print(f"Valor de X dentro de la función local: {x}")
    
funcion_local()

def funcion_global():
    global x #Pra modificar la variable global
    x= 30
    print(f"Valor de x dentro de la función global: {x}")
    
    
funcion_local()    
funcion_global()

print(f"Valor de x fuera de la función: {x}")