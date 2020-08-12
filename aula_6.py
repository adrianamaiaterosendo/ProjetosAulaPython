conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
conjunto_interseccao= conjunto.intersection(conjunto2)
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
# conjunto.add(5)
# conjunto.discard(2)
print(conjunto_uniao)
print(conjunto_interseccao)
print(conjunto_diferenca)
print (conjunto_dif_simetrica)

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5,6}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)
#superset é o inverso, ex b é um superconnunto de a
#para converter uma lista em conjunto (serve para remover duplicidade
lista = [1,2,3,4,5,5,5,5,8,8]
conjunto_numeros = set(lista)
print(conjunto_numeros)
