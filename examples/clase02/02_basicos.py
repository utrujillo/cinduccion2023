# variables y constantes en Python
saludo = "Hola mundo"
numero1 = 10
numero2 = 10.5
PI = 3.1416

# Salida de datos en python
print( saludo, numero1, numero2, PI )

# Entrada de datos en python
# entrada = input("Dame tu nombre: ")
# print("Tu nombre es: ", entrada)

# Verificando el tipo de datos
print( type(saludo) ) 
print( type(numero1) )

# Trabajando con cadenas
print( saludo +" "+ str( numero1 ) )
print( "%s %s" %(saludo, numero1) )

profesor = "Uziel Trujillo Colon"
menu = """
    Bienvenidos al curso de induccion
    impartido por %s
"""

print( menu %(profesor) )