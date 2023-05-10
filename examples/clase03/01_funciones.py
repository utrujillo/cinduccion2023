# Forma 1
def saludo():
    profesor = "Uziel Trujillo Colon"
    menu = """
        Bienvenidos al curso de induccion
        impartido por %s
    """
    print( menu %(profesor) )

saludo()

# Forma 2
def saludo2():
    profesor = "Juan Penas"
    menu = """
        Bienvenidos al curso de induccion
        impartido por %s
    """
    return menu %(profesor)

mensaje = saludo2()
print( mensaje )

# Forma 3
profesor = input("Cual es tu nombre: ")
def saludo3(profesor):
    menu = """
        Bienvenidos al curso de induccion
        impartido por %s
    """
    print( menu %(profesor) )

saludo3(profesor)