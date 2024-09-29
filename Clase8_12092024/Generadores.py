 # Ejemplo básico de un generador
 # generador que produce números de 1 al 5
 # Definición del generador:
 
def contador():
     # itera sobre los números del 1 al 5 
     for i in range(1, 6):   # itera sobre los números del 1 al 5, no contempla el 6
         yield i #produce el valor de i y pausa la ejecución
         
# crear una instancia para el generador

gen = contador() # gen es un objeto generador

# iterar sobre los valores producticos por el mismo generador

for numero in gen:
    print(numero) # imprime cada uno de los números producido por el generador
    

     
 