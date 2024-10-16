import numpy
class Player:
    def __init__(self, name):
        self.name = name 
        self.pokemon_array = numpy.array([])
    def choose_pokemon(self, pokemon):
        self.pokemon_array = numpy.append(self.pokemon_array, pokemon)
        