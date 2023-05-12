# mouse = () # tupla
# mouse = [] # lista

mouse = {
    'color': 'Gris con rojo',
    'marca': 'Logitec',
    'izquierdo': True,
    'derecho': True,
    'scroll': True,
    'precision': 2000
} # diccionario

mouse2 = {
    'color': 'Blanco',
    'marca': 'Mac',
    'izquierdo': True,
    'derecho': False,
    'scroll': True,
    'precision': 200
} # diccionario

mice = [ mouse, mouse2 ]

for raton in mice:
    print( "Precision %s" %(raton['precision']) )