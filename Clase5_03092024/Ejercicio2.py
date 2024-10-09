libro = {
"Titulo": "El Principito",
"Autor": "Antoine de Saint-Exupéry",
"Año de publicación": "1900",
"Género": "Fantasía"    
       
}

Titulo = libro["Titulo"]
Autor = libro["Autor"]
Ano = libro["Año de publicación"]
Genero = libro["Género"]

print(Titulo)
print(Autor)
print(Ano)
print(Genero)

#Actualizar el año

libro["Año de publicación"] = 2015

print("El diccionario antes de hacerle cambios: ")
print(Titulo)
print(Autor)
print(Ano)
print(Genero)

print("El diccionario después de hacerle cambios: ")

# Volvemos a obtener el valor actualizado
Ano = libro["Año de publicación"]

print(Ano)
