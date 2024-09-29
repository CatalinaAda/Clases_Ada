# Escribe un programa que asigna un mensaje a una variable resultado basado en una calificación (entre 0 y 100). Usa el operador ternario
# para asignar "Aprobado" si la calificación es mayor o igual a 60 y"Reprobado" en caso contrario

calificacion = int(input("Ingrese su calificación: "))

calificacion_final = "Aprobado" if calificacion >= 60 else "Reprobado"

print(calificacion_final)