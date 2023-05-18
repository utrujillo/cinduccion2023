
from Pokemon import *
from IElectrico import *

class Pikachu(Pokemon, IElectrico):
    def thunderPunch(self):
        print('Atacar con thunder punch')
    
    def doubleKick(self):
        print('Atacar con doubleKick')