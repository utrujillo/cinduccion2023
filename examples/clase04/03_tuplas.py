# Una vez definida no se puede agregar ningun valor
valores = ( 'Python', True, "Javascript", 10 )
print(valores)

for valor in valores:
    print("Valor %s" %(valor))

for indice, valor in enumerate(valores):
    print("Indice %s Valor %s" %(indice, valor))

print( valores[1] )