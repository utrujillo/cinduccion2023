import random

class Pokemon:
    def __init__(self, id, name, weight, size):
        self.id = id
        self.name = name.capitalize()
        self.weight = weight
        self.size = size
        self.base_experience = random.randint(0, 250)

    def getPokemon(self):  
        pokemon = f'''
            ID {self.id}
            Pokemon {self.name}
            Peso {self.weight:.2f}   Altura {self.size:.2f}
            Experiencia base {self.base_experience}
        '''
        return pokemon

    
pikachu = Pokemon(80, "pikachu", 67.23213, 110.453)
print( pikachu.base_experience )

dataPokemon = pikachu.getPokemon()
print( dataPokemon )