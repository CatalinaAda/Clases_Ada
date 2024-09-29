# crear un diccionario

persona = {
    "Nombre" : "Verónica",
    "Edad" : 25,
    "Ciudad": "Buenos Aires"
}

# usar el método. get

nombre = persona.get("Nombre")
edad = persona.get("Edad")
ciudad = persona.get("Ciudad")

print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)

# intentar acceder a una clave que no existe usando .get

pais = persona.get("Pais")
print("Pais: ", pais)

# Usar get con un valor predeterminado si la clave no existe

pais_con_valor_predeterminado = persona.get("pais", "No identificado")

print("País con valor predeterminado: ", pais_con_valor_predeterminado)



