nombre = "Uziel Trutillo Colon"
print("Original %s" %(nombre))

nombre = nombre.lower()
print( "Cadena %s" %(nombre) )

nombre = nombre.upper()
print( "Cadena %s" %(nombre) )

nombre = nombre.capitalize()
print( "Cadena %s" %(nombre) )

nombre = nombre.replace("t", "T")
print( "Reemplazar %s" %(nombre) )

print( "Indice 3: es %s" %(nombre[3]))

print( "Rango de cadena [0:4] %s" %(nombre[0:4]) )
print("Invertir cadena [::-1] %s" %(nombre[::-1]))