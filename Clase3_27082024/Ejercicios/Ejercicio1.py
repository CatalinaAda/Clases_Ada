# Escribe un programa que cuente cuántas veces aparece un número
# específico en una lista.
# Instrucciones:
# • Define una lista de números predefinida o pídele al usuario que ingrese los números.
# • Pide al usuario que ingrese un número a buscar.
# • Usa el método count() para determinar cuántas veces aparece el
# número en la lista.
# • Muestra el resultado

lista_numeros = [1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 2, 1, 4, 5]
numero_buscado = int(input("Ingrese el número que desea: "))
lista_numeros.count(numero_buscado)
print("El número", numero_buscado, "aparece", lista_numeros)
