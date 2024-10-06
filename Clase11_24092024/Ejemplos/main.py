# importamos el módulo completo 
import operaciones
print(f"Suma (Import completo): {operaciones.sumar(2,3)}")

#renombrando el módulo
import operaciones as op
print(f"Suma (Import renombrado): {op.restar(5,2)}")

#Importar una función especifica
from operaciones import multiplicar
print(f"Multiplicación (Función específica): {multiplicar(3,2)}")

# renombramos las funcion específica

from operaciones import sumar as suma
print(f"Suma (Función renombrada): {suma(10,70)}")

# Importando todo el módulo con  *

from operaciones import *

print(F"Resta (Import *): {restar(30,5)}")

"C:\Users\User\Desktop\ADA_TRABAJOS_PYTHON\Clase12_CatalogoPeliculas"








