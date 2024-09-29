# Crear un diccionario

persona = {
    "Nombre" : "Alejandra",
    "Edad" : 30,
    "Ciudad" : "Merida"
}


#Usamos pop para eliminar la clave edad y obtener su valor

valor_eliminado = persona.pop("Edad")

#Imprimimos el valor eliminado y el diccionario resultante

print("Valor eliminado: ", valor_eliminado)

print("Diccionario después de eliminar edad: ", persona)


# Usar pop con una clave que no existe y un valor por defecto

valor_inexistente = persona.pop("Pais", "No especificado")

print("Valor cuando la clave no existe: ", valor_inexistente)