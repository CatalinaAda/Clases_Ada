# Ejercicio 5: Manejo de Matrículas en una Tupla
# • Crea una tupla llamada matriculas con los siguientes números de
# matrícula: (101, 102, 103, 104, 105).
# • Usa el método count para contar cuántas veces aparece el número
# de matrícula 102 en la tupla.
# • Usa el método index para encontrar la posición del número de
# matrícula 104 en la tupla.

matricula = (101, 102, 103, 104, 105)
numero_matricula = matricula.count(102)

print("El número de veces que aparece la matrícula 102 es: ", numero_matricula)

posicion_104 = matricula.index(104)

print("La matrícula 104 está en la posición: ", posicion_104)



