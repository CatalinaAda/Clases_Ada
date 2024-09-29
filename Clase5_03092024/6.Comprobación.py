# Crear un diccionario 

persona = {
    "Nombre" : "Emilia",
    "Edad" : 33,
    "Ciudad": "Caba"
}

#Comprobar si una clave existe en el diccionario antes de acceder a su valor

clave = "edad"

if clave in persona:
    valor = persona[clave]
    print(f"El valor de {clave} es: {valor}")
    
else:
    print(f"La clave {clave} no existe en el diccionario")
    
# Clave inexistente

clave_inexistente = "pais"

if clave_inexistente in persona:
    valor = persona[clave_inexistente]
    print(f"El valor de la {clave_inexistente} es: {valor}")
else:
    print(f"El valor de la clave {clave_inexistente} no existe")
    
# buscar una clave con in solamente

persona_2 = {
    "nombre": "Emilia",
    "edad": 33,
    "ciudad": "CABA"
}
print("nombre" in persona_2)