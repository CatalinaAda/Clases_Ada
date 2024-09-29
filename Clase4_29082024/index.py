# crear una tupla con varios elementos

mi_tupla = (10, 20, 30, 40, 50)

#Encontrar la posición del número 30 en la tupla
indice_de_30 = mi_tupla.index(30)

print("El número 30 se encuentra en la posición: ", indice_de_30)



#Verificar si un vaor está en la tupla antes de buscar su indice

valor_buscado = 60

if valor_buscado in mi_tupla:
    #Si el valor está en la tupla, encontrar su indice
    indice_del_valor = mi_tupla.index(60)
    print(f"El número {valor_buscado} se encuwentra en {indice_del_valor}")
else:
    #Si el valor no está en la tupla, mostrar el mensaje
    print(f"El número {valor_buscado} no estáa en la tupla")