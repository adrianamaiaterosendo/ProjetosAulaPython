lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']
print(lista_animal[1])

print(sum(lista))
print(max(lista))
#busca por ordem alfabetica se for string
if 'lobo' in lista_animal:
    print('Existe um gato na lista')
else:
    print('não existe na lista')
    lista_animal.append('lobo')
#para incluir append e pafa retirar pop com a posição e remove com o nome

print(lista_animal)
novalista = lista_animal *3
print (novalista)
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)
lista_animal.reverse()
print(lista_animal)

#tupla, eu coloco os dados entre parenteses e não altera posição
#print.len traz a quantidade de elementos da tupla
#print.tuple converte a lista para tupla
# o list faz o inverso

