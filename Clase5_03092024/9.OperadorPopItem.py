# creamos un diccionario


persona = {
    "Nombre" : "Emilia",
    "Edad" : 33,
    "Ciudad": "Caba",
    "Profesión": "Veterinaria"
}


#imprimir el diccionario original 

print("Diccionario original: ", persona)

#Usamos pop item para eliminar y obtener el último par Clave-Valor

ultimo_elemento = persona.popitem()

#Imprimirmos el par clave-valor

print("Ultimo par clave-valor: ", ultimo_elemento)

#Imprimir el diccionario después del popitem

print("Diccionario después de usar pop_item ", persona)
