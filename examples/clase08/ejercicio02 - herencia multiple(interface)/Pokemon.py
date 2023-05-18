import random

class Pokemon:
    def __init__(self, id, name, weight, size):
        self.id = id
        self.name = name.capitalize()
        self.weight = weight
        self.size = size
        self.base_experience = random.randint(0, 250)

    def getDataPokemon(self):  
        pokemon = f'''
            ID {self.id}
            Pokemon {self.name}
            Peso {self.weight:.2f}   Altura {self.size:.2f}
            Experiencia base {self.base_experience}
        '''
        return pokemon