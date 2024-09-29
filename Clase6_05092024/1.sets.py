# Gestión de asistentes a un evento
# Crear un programa que administre una lista de asistentes a evento sin permitir duplicados
# y que realice operaciones entre dos listas


invitados_viernes = {"Ana", "Carlos","Pedro", "Luis", "Clara"}
invitados_sabado = {"Carlos", "Luis","Sofia", "Maria", "Pedro"}

#Mostar a los invitados únicos que asisten el viernes

print("invitados_viernes:", invitados_viernes)

#Mostar a los invitados únicos que asisten el sábado
print("invitados sábado:", invitados_sabado)


# Mostar la unión (quien asistió la menos una vez)
todos_asistentes = invitados_sabado | invitados_viernes
print("Asistentes de los dos días: ", todos_asistentes)

#Mostar la inteseccion (quién asistió ambos días)

solo_viernes = invitados_viernes - invitados_sabado
print("Asistentes solo viernes: ", solo_viernes)


# Agregar un nuevo invitado el sábadp
invitados_sabado.add("Miguel")

print("Nueva lista de invitados: ", invitados_sabado)

#eliminar un invitado que canceló
invitados_sabado.remove("Maria")
print("Invitados del sábado después de eliminar un invitado: ", invitados_sabado)




