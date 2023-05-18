from Pikachu import *
from Raichu import *

def run():
    pikachu = Pikachu(80, 'pikachu', 68, 100)
    pikachu.ataqueNuevo()
    
    raichu = Raichu(81, 'Raichu', 100, 400)
    print( raichu.getDataPokemon() )
    raichu.ataqueNuevo()

if __name__ == '__main__':
    run()