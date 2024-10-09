# Desarrolla un programa que haga lo siguiente:
# 1.Usar un bucle while para pedir al usuario que ingrese números hasta que se ingrese el número 0.
# 2.Usar un bucle for para calcular la suma de los números ingresados, excluyendo el 0.


def ingresando_numeros():
    
    lista_numeros = []
    
    while True:
        numero = int(input("Ingresa tu número entero aquí: "))
        if numero == 0:
            break
        else:
            lista_numeros.append(numero)
    
    suma = 0
    
    for i in lista_numeros:
        suma += i
        
    return suma

suma = ingresando_numeros()

print(f"La suma de los números ingresados es: {suma}")
            
