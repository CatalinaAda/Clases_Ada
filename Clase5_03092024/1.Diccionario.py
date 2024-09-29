 #Ejemplo de diccionario
 
diccionario_vacio = {}
print("Ejemplo de un diccionario vacío: ", diccionario_vacio)

# Ejemplo básico de un diccionario

persona = {
    "nombre" : "María",    #Atributo : #Valor
    "Edad" : 30,
    "Casada" : False,
    "Hijos" : ["Ana", "Luis"], #Lista dentro del diccionario / Clave: Str, valor, una lista
    "Direccion" : {                    #Clave es un string, el valor es un diccionario adicional
        "Calle" : "La Gran Vía",
        "Ciudad": "Madrid",
        
    }
}
print("Ejemplo de diccionario básico", persona)

#Ejemplo de diccionario con valores de distintos tipos

diccionario_mixto = {
    "Nombre" : "Alejandra",
    1: [2, 3, 4],    #Lista con clave como entero - Valor es un string
    (2, 3) : "Tupla como clave"  #Clave es una tupla
       
}
print("Ejemplo de diccionario mixto: ", diccionario_mixto)


