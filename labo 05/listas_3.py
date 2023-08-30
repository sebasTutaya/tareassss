lista_1 = [1,2,3,4,5,6,7,8,9,10]
lista_2 = [5,6,7,8,9,10,11,12,13,14,15]
lista_3 = [10,11,12,13,14,15,16,17,18,19,20]
#convertir la lista en conjuntos
lista_conv_1 = set(lista_1)
lista_conv_2 = set(lista_2)
lista_conv_3 = set(lista_3)
print(lista_conv_1)
print(lista_conv_2)
print(lista_conv_3)
#numero presente en las tres listas
A = lista_conv_1.intersection(lista_conv_2).intersection(lista_conv_3)
print("interseccion: ", A)
#presente en al menos una de las primeras listas
B = lista_conv_1.union(lista_conv_2).union(lista_conv_3)
print("B: ", B)
#diferencia entre lista 1 y lista 2
C = lista_conv_1.difference(lista_conv_3)
print("diferencia: ", C)
#convertir en tuplas

list_1 = list(A)
list_2 = list(B)
list_3 = list(C)

tpl_1 = tuple(list_1)
tpl_2 = tuple(list_2)
tpl_3 = tuple(list_3)

#sumar el primer y ultimo elemento de cada tupla
suma1 = tpl_1[0] + tpl_1[-1]
print("suma1: ", suma1)
suma2 = tpl_2[0] + tpl_2[-1]
print("suma2: ", suma2)
suma3 = tpl_3[0] + tpl_3[-1]
print("suma3: ", suma3)
