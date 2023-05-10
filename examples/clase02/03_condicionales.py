import random

# edad = int( input("Cual es tu edad? ") )
# print( type(edad) )
edad = random.randint(0, 100)

if ( edad > 18 ):
    print("Eres mayor de edad, tu edad es: %i" %(edad))
elif( edad == 18 ):
    print("Eres mayor de edad apenas")
else:
    print("Eres menor de edad, tu edad es: %i" %(edad))