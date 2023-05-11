# Listas si me permiten agregar o eliminar informacion
nombre = "Juan penas"
lista = [ 'Hola', 4, 4.5, True ]
lista2 = [ 100, False, 'segunda lista', nombre ]
lista4 = [1, 2, 1000]
print( lista )

# Accediendo a un valor especifico
print( lista[3] )

# Agregando datos a la lista
lista.append(lista4)
print(lista)

# Eliminar datos de la lista
lista.pop(1)
print(lista)

# Combinando listas
lista3 = lista + lista2
print( lista3 )

print(lista[3][2])

for indice, valor in enumerate(lista):
    print("Indice %i valor %s" %(indice, valor))


matrizA = [
    [1,2],
    [4,5],
    [7,8]
]

print(matrizA)