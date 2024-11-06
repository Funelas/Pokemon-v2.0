import numpy
class Player:
    def __init__(self, name):
        self.name = name 
        self.pokemon_array = numpy.array([])
        self.pokemon_name_array = numpy.array([], dtype= "U20")
        self.points = 22
        self.used_potions = 0
        self.used_poisons = 0
        self.number_of_wins = 0
    def choose_pokemon(self, pokemon):
        self.pokemon_array = numpy.append(self.pokemon_array, pokemon)
        self.pokemon_name_array = numpy.append(self.pokemon_name_array, pokemon.name)
    def all_pokemon_used(self):
        return all(pokemon.used for pokemon in self.pokemon_array)
    def pokemon_died(self, pokemon):
        self.pokemon_name_array = self.pokemon_name_array[self.pokemon_name_array != pokemon]
        print(f"{pokemon} has run out of health. Removing them from {self.name}'s inventory and delivering them to the Pokemon Centre.")
    def total_health(self):
        return sum(pokemon.health for pokemon in self.pokemon_array)