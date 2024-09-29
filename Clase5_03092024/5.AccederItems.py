# crear ottro diccionario

persona = {
    "Nombre" : "Alejandra",
    "Edad" : 30,
    "Ciudad" : "Merida"
}

# usamos el método .list()

pares_clave_valor = persona.items()

print("Pares claves valor:", pares_clave_valor)
#convertir valores en una lista

valores_lista = list(pares_clave_valor)
print("Valores como lista: ",(valores_lista))
