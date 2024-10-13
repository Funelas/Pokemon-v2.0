import player
import time 
import numpy as np

# Define the structured data type for the Pokémon array
pokemon_dtype = np.dtype([
    ('name', 'U20'),              # Name of the Pokémon (up to 20 characters)
    ('element', 'U10'),           # Element of the Pokémon (up to 10 characters)
    ('health', 'i4'),             # Health (integer)
    ('power', 'i4'),              # Power (integer)
    ('healing_potions', 'i4'),    # Healing potions (integer)
    ('poisons', 'i4'),            # Poisons (integer)
    ('strong_against', 'U50'),    # Strong against type (up to 50 characters)
    ('weak_against', 'U50'),      # Weak against type (up to 50 characters)
])

# Creating the Pokémon structured array
pokemon_array = np.array([
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
    ("Nidoran♀", "Poison", 55, 40, 3, 2, "Fairy", "Psychic"),
    ("Nidoran♂", "Poison", 46, 57, 2, 2, "Fairy", "Psychic"),
    ("Golbat", "Poison", 75, 80, 2, 2, "Grass", "Electric"),
    ("Zubat", "Poison", 40, 45, 3, 2, "Grass", "Electric"),
    ("Grimer", "Poison", 80, 80, 2, 2, "Fairy", "Psychic"),
    ("Geodude", "Rock", 40, 80, 2, 1, "Fire", "Water"),
    ("Hitmonlee", "Fighting", 50, 120, 2, 3, "Normal", "Psychic"),
    ("Electrode", "Electric", 60, 50, 3, 3, "Water", "Ground"),
    ("Alakazam", "Psychic", 55, 120, 2, 5, "Fighting", "Bug"),
], dtype=pokemon_dtype)

# Grouping based on power and creating separate arrays
overpowered_pokemon = pokemon_array[(pokemon_array['power'] >= 100)]
mid_tier_pokemon = pokemon_array[(pokemon_array['power'] >= 50) & (pokemon_array['power'] < 100)]
weakest_pokemon = pokemon_array[(pokemon_array['power'] < 50)]

# Creating separate arrays for each group
overpowered_array = np.array(overpowered_pokemon)
mid_tier_array = np.array(mid_tier_pokemon)
weakest_array = np.array(weakest_pokemon)

def slow_type(passage, delay = 0, ending = False):
    delay = delay # Set to 0 to make every thing instant
    for letter in passage:
        print(letter, end= "", flush= True)
        time.sleep(delay)
    if ending:
        print(end = "")
    else:
        print()
slow_type("Welcome to Pokémon Battle Royale: Power, Strategy, and Fatigue!", 0.1)
slow_type("Please Enter your Name",0.1)
player_1 = player.Player(str(input("Player 1: ")))
player_2 = player.Player(str(input("Player 2: ")))

slow_type("Quick Mechanics:\nEach Player selects an agreed number of pokemons.\nPlayers will take turns in selecting a pokemon.\nSelected pokemons will not be available for the next pickings.\nOn the fight round, each players will choose a pokemon to fight with the other player.\nNOTE: Players can use consumable potions and poisons before commencing to the fight\nThe pokemon with the higher power will win.\nWhen a player already used all of their pokemons even with all of them alive, they will now have the option to run away or stay.\nAt the end of the overall fight (either due to a player having no more usable pokemons or a player running away), the player with the higher total of pokemon health wins.\n", 0.01)

slow_type("Trainers, Are you ready?\nProgram commencing in ", 0.05, True)
slow_type("3...2...1...", 0.1)
slow_type("Good Luck!")

while True:
    slow_type("Before choosing your pokemons, let's first settle how many pokemons you all would like to have for this match. Enter your preferred number of pokemons to this match ( 3 or 4 )")
    while True:
        player_1_decision = int(input("Player 1: "))
        if player_1_decision not in [3,4]:
            slow_type("Invalid Input. Please enter only between 3 and 4", 0.05)
            continue
        else:
            break
    while True:
        player_2_decision = int(input("Player 2: "))
        if player_2_decision not in [3,4]:
            slow_type("Invalid Input. Please enter only between 3 and 4", 0.05)
            continue
        else:
            break
    if player_1_decision != player_2_decision:
        slow_type("Since the two of you have chosen different numbers, we will be having a rock-paper-scissors match to know which number we will be choosing.", 0.05)
        slow_type("R - Rock\nP - Paper\nS - Scissors", 0.05)
        slow_type("Please Enter Your Preffered Weapon", 0.05)
        while True:
            weapons = ['s', 'r', 'p']
            weapon_names = ["Scissors", "Rocks", "Paper"]
            while True:
                player_1_weapon = str(input("Player 1: ")).lower()
                if player_1_weapon not in weapons:
                    slow_type("Invalid Input. Please enter only between the given selection", 0.05)
                    continue 
                else:
                    print("\033[F\033[K", end = "")
                    break 
            while True:
                player_2_weapon = str(input("Player 2: ")).lower()
                if player_2_weapon not in weapons:
                    slow_type("Invalid Input. Please enter only between the given selection", 0.05)
                    continue 
                else:
                    print("\033[F\033[K", end = "")
                    break

            if (player_1_weapon == 'r' and player_2_weapon == "s") or (player_1_weapon == 's' and player_2_weapon == "p") or (player_1_weapon == 'p' and player_2_weapon == "r"):
                slow_type(f"Player 1's {weapon_names[weapons.index(player_1_weapon)]} beats Player 2's {weapon_names[weapons.index(player_2_weapon)]}. Therefore the pokemon battle will follow {player_1_decision} pokemons per trainer", 0.05)
                number_of_pokemon = player_1_decision
                break
            elif player_1_weapon == player_2_weapon:
                slow_type(f"Both Player 1 and Player 2 picked {weapon_names[weapons.index(player_1_weapon)]}. Recommencing the match...", 0.05)
                continue
            else:
                slow_type(f"Player 2's {weapon_names[weapons.index(player_2_weapon)]} beats Player 1's {weapon_names[weapons.index(player_1_weapon)]}. Therefore the pokemon battle will follow {player_2_decision} pokemons per trainer", 0.05)
                number_of_pokemon = player_2_decision
                break 
    else:
        number_of_pokemon = player_1_decision
    slow_type("Next that we need to decide is who gets first to choose their pokemon. Now we are commencing a coin toss. Choose your preffered coin side", 0.05)
    slow_type("H ")
    player_1_coin = 