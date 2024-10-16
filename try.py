import numpy 
import tabulate
import pokemon
pokemon_dtype = numpy.dtype([
    ("name", "U20"),
    ("element", "U20"),
    ("health", "i4"),
    ("power", "i4"),
    ("potion", "i4"),
    ("poison", "i4"),
    ("strong_against", "U50"),
    ("weak_against" , "U50")
])
pokemon_array = numpy.array([
                ("Pikachu", "Electric", 35, 55, 3, 2, "Water", "Ground"),
                ("Charmander", "Fire", 39, 52, 2, 3, "Grass", "Water, Rock"),
                ("Bulbasaur", "Grass", 45, 49, 3, 2, "Water", "Fire, Flying"),
                ("Squirtle", "Water", 44, 48, 3, 2, "Fire", "Grass, Electric"),
                ("Jigglypuff", "Normal", 115, 45, 4, 1, "", "Fighting"),
                ("Eevee", "Normal", 55, 55, 3, 2, "", "Fighting"),
                ("Snorlax", "Normal", 160, 110, 2, 3, "", "Fighting"),
                ("Gengar", "Ghost", 60, 65, 3, 4, "Psychic", "Ghost"),
                ("Mewtwo", "Psychic", 106, 110, 2, 5, "Fighting", "Bug"),
                ("Lapras", "Water", 130, 85, 3, 2, "Fire", "Electric"),
                ("Togepi", "Fairy", 35, 40, 4, 1, "Dragon", "Poison"),
                ("Psyduck", "Water", 50, 52, 3, 2, "Fire", "Grass"),
                ("Onix", "Rock", 35, 45, 2, 2, "Fire", "Water, Fighting"),
                ("Machop", "Fighting", 70, 80, 2, 3, "Normal", "Psychic"),
                ("Magikarp", "Water", 20, 10, 5, 0, "Fire", "Electric"),
                ("Dragonite", "Dragon", 91, 134, 2, 4, "Grass", "Ice"),
                ("Lucario", "Fighting", 70, 110, 2, 3, "Normal", "Fighting"),
                ("Caterpie", "Bug", 45, 30, 3, 0, "Grass", "Fire"),
                ("Rattata", "Normal", 30, 56, 2, 2, "", "Fighting"),
                ("Clefairy", "Fairy", 70, 45, 3, 2, "Dragon", "Steel"),
                ("Pidgey", "Normal", 40, 45, 3, 1, "Grass", "Electric"),
                ("Machoke", "Fighting", 80, 100, 2, 3, "Normal", "Psychic"),
                ("Ponyta", "Fire", 50, 85, 2, 2, "Grass", "Water"),
                ("Sandshrew", "Ground", 50, 75, 2, 2, "Electric", "Water"),
                ("Nidoran", "Poison", 55, 40, 3, 2, "Fairy", "Psychic"),
                ("Golbat", "Poison", 75, 80, 2, 2, "Grass", "Electric"),
                ("Zubat", "Poison", 40, 45, 3, 2, "Grass", "Electric"),
                ("Grimer", "Poison", 80, 80, 2, 2, "Fairy", "Psychic"),
                ("Geodude", "Rock", 40, 80, 2, 1, "Fire", "Water"),
                ("Hitmonlee", "Fighting", 50, 120, 2, 3, "Normal", "Psychic"),
                ("Electrode", "Electric", 60, 50, 3, 3, "Water", "Ground"),
                ("Alakazam", "Psychic", 55, 120, 2, 5, "Fighting", "Bug"),
            ], dtype=pokemon_dtype)
high_powered_pokemons = pokemon_array[pokemon_array["power"] >= 100]
mid_powered_pokemons = pokemon_array[(pokemon_array["power"] > 50) & (pokemon_array["power"] < 100)]
low_powered_pokemons = pokemon_array[pokemon_array["power"] < 50]
high_powered_pokemons_names = numpy.array([pokemon["name"] for pokemon in high_powered_pokemons])
mid_powered_pokemons_names = numpy.array([pokemon["name"] for pokemon in mid_powered_pokemons])
low_powered_pokemons_names = numpy.array([pokemon["name"] for pokemon in low_powered_pokemons])

headers = ["High-Powered Pokemons\nCost = 11", "Mid-Powered Pokemons\nCost = 7", "Low-Powered Pokemons\nCost = 1"]
data = zip(high_powered_pokemons_names, mid_powered_pokemons_names, low_powered_pokemons_names)
table = tabulate.tabulate(data, headers, tablefmt = "pretty")
print(table)
print(pokemon_array[pokemon_array["name"] == "Snorlax"])
# print(high_powered_pokemons)
# print(mid_powered_pokemons)
# print(low_powered_pokemons)
# for i in range(len(pokemon_array[3] >= 100)):
#     print(f"{i+1}: {pokemon_array[i][0]}")