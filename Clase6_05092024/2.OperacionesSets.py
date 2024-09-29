#Crear conjuntos

conjunto_a={1,2,3,4}
conjunto_b={3,4,5,6}
conjunto_c={7,8,9}

# Subconjuntos
es_subconjunto = conjunto_a.issubset(conjunto_b)
print("Es conjunto_a un subconjunto del conjunto_b: ", es_subconjunto)

#Superconjunto

es_superconjunto = conjunto_b.issuperset(conjunto_a)

print("Es conjunto B, un super conjunto del conjunto a: ", es_superconjunto)

#Disconjuntos

son_disconjuntos = conjunto_a.isdisjoint(conjunto_c)

print("Son conjunto_a y conjunto_c disjuntos: ", son_disconjuntos)

#Simetria

simetria = conjunto_a.symmetric_difference(conjunto_b)

print("Diferencia simétrica entre conjunto_a y conjunto_b: ", simetria)


#unión update
conjunto_a.update(conjunto_b)
print("Conjunto_a despues de la unión con conjunto_b: ", conjunto_a)

# Intersección Updated
conjunto_a.intersection_update(conjunto_b)
print("Conjunto_a despues de la intresección con conjunto_b:", conjunto_a)


#Difference update
conjunto_b.difference_update(conjunto_c)
print("Conjunto_b después de la diferencia con conjunto_c: ", conjunto_a)

#Symetricdifference

conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_b)


