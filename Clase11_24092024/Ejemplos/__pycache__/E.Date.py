import datetime


#Fecha actual

Fecha_actual = datetime.date.today()

print(f"Fecha actual: {Fecha_actual}")

#Hora actual

hora_actual = datetime.datetime.now().time()
print(f"Hora actual: {hora_actual}")

#FEcha y hora actual

fecha_hora_actual = datetime.datetime.now()

print(F"Fecha y hora actuales: {fecha_hora_actual}")

#Crear una fecha y una hora específica

mi_fecha = datetime.date(2024, 8, 22)
mi_hora = datetime.time(14, 30, 0)

print(F"Fecha específica: {mi_fecha}")
print(F"Hora específica: {mi_hora}")

#Cálculos con fechas : sumar 10 días a la fecha actual

diferencia = datetime.timedelta(days=10)

nueva_fecha = Fecha_actual + diferencia
print(F"Mi nueva fecha es: {nueva_fecha}")






