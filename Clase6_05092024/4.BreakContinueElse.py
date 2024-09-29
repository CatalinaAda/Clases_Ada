# Programa que pide número hasta que se ingrese un número negativo

# Inicializamos la variable suma para acumular la suma de los números positivos ingresados

suma = 0

# inicializamos un ciclo infinito usando while true

while True:
    #Solicitamos al usuario ingresar un número, la entrada se convierte en número entrero
    entrada = int(input("Introduce un número (negativo para terminar): "))
    
    # Verificamos si el número ingresado es negativo
    
    if entrada < 0:
        # Si el número es negativo, salimos del ciclo usando 
        break
    #sumamos el número positivo ingresado a la variable suma
    
    suma += entrada
    
    #Verificar si el número inhresado es par
    
    if entrada % 2 == 0:
    #Si el número es par, usamos continue para saltar la impresión y pasar a la siguoente iteracion del ciclo
        continue
    
    print("Número impar ingresado:", entrada)

# si el número ingresado no es par(es impar) se ejecuta esta línea

else:
    print("La suma de los números ingresados es: ", suma)
    
    

