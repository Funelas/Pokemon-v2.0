import player
from pokemon import *
import time 
import random
import numpy
import tabulate
def slow_type(passage, delay = 0, ending = False):
    delay = 0 # Set to 0 to make every thing instant
    for letter in passage:
        print(letter, end= "", flush= True)
        time.sleep(delay)
    if ending:
        print(end = "")
    else:
        print()
def show_history(values, player_1_name, player_2_name):
    header = ["Match\nNo.", f"{player_1_name}'s Pokemon\nvs.\n{player_2_name}'s Pokemon", f"{player_1_name}'s Pokemon\nPre-Health", f"{player_2_name}'s Pokemon\nPre-Health", f"{player_1_name}'s Pokemon\nFinal Power",f"{player_2_name}'s Pokemon\nFinal Power", "Battle\nOutcome",f"{player_1_name}'s Pokemon\nPost-Health", f"{player_1_name}'s Pokemon\nPost-Health" ]
    history_table = tabulate.tabulate(values, header, tablefmt= 'pretty')
    print(history_table)
def show_pokemon_status(values):
    data = [values]
    header = ["Name", "Element", "Current Health", "Current Power", "Number of\nPotions", "Number of\nPoisons", "Strength", "Weakness"]
    table = tabulate.tabulate(data, header, tablefmt = "pretty")
    print(table)
def show_summary(player_1, player_2):
    header = [f"{player_1.name}\nPokemon Name", f"{player_1.name}\nPokemon's Health", f"{player_2.name}\nPokemon Name", f"{player_2.name}\nPokemon's Health"]
    values = list(zip((i.name for i in player_1.pokemon_array), (i.health for i in player_1.pokemon_array), (i.name for i in player_2.pokemon_array), (i.health for i in player_2.pokemon_array)))
    values.append(["Total Health: ", f"{player_1.total_health()}", "Total Health: ", f"{player_2.total_health()}"])
    summary_table = tabulate.tabulate(values, header, tablefmt= 'pretty')
    print(summary_table)
pokemon_dtype = numpy.dtype([
    ("name", "U20"),
    ("element", "U20"),
    ("health", "i4"),
    ("power", "i4"),
    ("potion", "i4"),
    ("poison", "i4"),
    ("strong_against", "U50"),
    ("weak_against", "U50"),
    ("cost", "i4")  # Added cost as a new field
])

# Create the Pokémon array with the updated structure
pokemon_array = numpy.array([
    ("Pikachu", "Electric", 63, 87, 2, 3, "Water", "Ground", 7),
    ("Charmander", "Fire", 69, 81, 3, 2, "Grass", "Water, Rock", 7),
    ("Bulbasaur", "Grass", 51, 69, 4, 3, "Water", "Fire, Flying", 1),
    ("Squirtle", "Water", 53, 67, 4, 3, "Fire", "Grass, Electric", 1),
    ("Jigglypuff", "Normal", 62, 58, 4, 3, "None", "Fighting", 1),
    ("Eevee", "Normal", 67, 83, 2, 3, "None", "Fighting", 7),
    ("Snorlax", "Normal", 98, 82, 3, 2, "None", "Fighting", 12),
    ("Gengar", "Ghost", 57, 93, 2, 3, "Psychic", "Ghost", 7),
    ("Mewtwo", "Psychic", 73, 107, 3, 2, "Fighting", "Bug", 12),
    ("Lapras", "Water", 89, 61, 3, 2, "Fire", "Electric", 7),
    ("Togepi", "Fairy", 38, 82, 4, 3, "Dragon", "Poison", 1),
    ("Psyduck", "Water", 63, 87, 2, 3, "Fire", "Grass", 7),
    ("Onix", "Rock", 49, 71, 4, 3, "Fire", "Water, Fighting", 1),
    ("Machop", "Fighting", 77, 73, 2, 3, "Normal", "Psychic", 7),
    ("Magikarp", "Water", 44, 76, 4, 3, "Fire", "Electric", 1),
    ("Dragonite", "Dragon", 86, 94, 3, 2, "Grass", "Ice", 12),
    ("Lucario", "Fighting", 67, 113, 2, 3, "Normal", "Fighting", 12),
    ("Caterpie", "Bug", 53, 67, 4, 3, "Grass", "Fire", 1),
    ("Rattata", "Normal", 67, 83, 2, 3, "None", "Fighting", 7),
    ("Clefairy", "Fairy", 57, 63, 4, 3, "Dragon", "Steel", 1),
    ("Pidgey", "Normal", 47, 73, 4, 3, "Grass", "Electric", 1),
    ("Machoke", "Fighting", 73, 107, 2, 3, "Normal", "Psychic", 12),
    ("Ponyta", "Fire", 77, 73, 3, 2, "Grass", "Water", 7),
    ("Sandshrew", "Ground", 83, 67, 2, 3, "Electric", "Water", 7),
    ("Nidoran", "Poison", 49, 71, 4, 3, "Fairy", "Psychic", 1),
    ("Golbat", "Poison", 67, 83, 2, 3, "Grass", "Electric", 7),
    ("Zubat", "Poison", 57, 63, 4, 3, "Grass", "Electric", 1),
    ("Grimer", "Poison", 71, 79, 3, 2, "Fairy", "Psychic", 7),
    ("Geodude", "Rock", 77, 73, 2, 3, "Fire", "Water", 7),
    ("Hitmonlee", "Fighting", 92, 88, 2, 3, "Normal", "Psychic", 12),
    ("Electrode", "Electric", 57, 93, 3, 2, "Water", "Ground", 7),
    ("Alakazam", "Psychic", 93, 87, 2, 3, "Fighting", "Bug", 12),
], dtype=pokemon_dtype)

# Display the updated array

def show_pokemon_table(excluded_names):
    # Exclude chosen Pokémon names from each category
    high_powered_pokemons = pokemon_array[(pokemon_array["cost"] == 12) & (~numpy.isin(pokemon_array["name"], excluded_names))]
    mid_powered_pokemons = pokemon_array[(pokemon_array["cost"] == 7) & (~numpy.isin(pokemon_array["name"], excluded_names))]
    low_powered_pokemons = pokemon_array[(pokemon_array["cost"] == 1) & (~numpy.isin(pokemon_array["name"], excluded_names))]

    # Get names of Pokémon for each power category
    high_powered_pokemons_names = numpy.array([pokemon["name"] for pokemon in high_powered_pokemons])
    mid_powered_pokemons_names = numpy.array([pokemon["name"] for pokemon in mid_powered_pokemons])
    low_powered_pokemons_names = numpy.array([pokemon["name"] for pokemon in low_powered_pokemons])

    # Pad arrays to ensure equal length
    max_len = max(len(high_powered_pokemons_names), len(mid_powered_pokemons_names), len(low_powered_pokemons_names))
    high_powered_pokemons_names = numpy.pad(high_powered_pokemons_names, (0, max_len - len(high_powered_pokemons_names)), constant_values="")
    mid_powered_pokemons_names = numpy.pad(mid_powered_pokemons_names, (0, max_len - len(mid_powered_pokemons_names)), constant_values="")
    low_powered_pokemons_names = numpy.pad(low_powered_pokemons_names, (0, max_len - len(low_powered_pokemons_names)), constant_values="")

    # Create headers and table
    headers = ["High-Powered Pokémons\nCost = 12", "Mid-Powered Pokémons\nCost = 7", "Low-Powered Pokémons\nCost = 1"]
    data = zip(high_powered_pokemons_names, mid_powered_pokemons_names, low_powered_pokemons_names)
    table = tabulate.tabulate(data, headers, tablefmt="pretty")

    print(table)

map_names = numpy.array(["Stadium", "Mystic Forest", "Volcano Ridge", "Crystal Cave", "Thunder Plains", "Snowfall Valley", "Desert Oasis", "Haunted Manor", "Sunny Park", "Ocean Depths"])
map_effects = numpy.array([[0.05, 0.1], [0.1, -0.1], [-0.05, 0.2], [0.15, 0.0], [0.0, 0.15], [-0.1, -0.05], [0.2, -0.1], [0.0, 0.25], [0.1, 0.1], [-0.05, -0.15]])



while True:
    history_values = []
    slow_type("Welcome to Pokémon Battle Royale: Power, Strategy, and Fatigue!", 0.1)
    slow_type("Please Enter your Name",0.1)
    player_1 = player.Player(str(input("Player 1: ")))
    player_2 = player.Player(str(input("Player 2: ")))
    slow_type("Quick Mechanics:\nEach Player selects an agreed number of pokemons.\nPlayers will take turns in selecting a pokemon.\nSelected pokemons will not be available for the next pickings.\nOn the fight round, each players will choose a pokemon to fight with the other player.\nNOTE: Players can use consumable potions and poisons before commencing to the fight\nThe pokemon with the higher power will win.\nWhen a player already used all of their pokemons even with all of them alive, they will now have the option to run away or stay.\nAt the end of the overall fight (either due to a player having no more usable pokemons or a player running away), the player with the higher total of pokemon health wins.\n", 0.01)
    slow_type("Trainers, Are you ready?\nProgram commencing in ", 0.05, True)
    slow_type("3...2...1...", 0.1)
    slow_type("Good Luck!")
    slow_type("Before choosing your pokemons, let's first settle how many pokemons you all would like to have for this match. Enter your preferred number of pokemons to this match ( 3 or 4 )")
    while True:
        player_1_decision = input(f"{player_1.name}: ")
        if player_1_decision not in ["3","4"]:
            slow_type("Invalid Input. Please enter only between 3 and 4", 0.05)
            continue
        else:
            break
    while True:
        player_2_decision = input(f"{player_2.name}: ")
        if player_2_decision not in ["3","4"]:
            slow_type("Invalid Input. Please enter only between 3 and 4", 0.05)
            continue
        else:
            break
    rps_match = False
    if player_1_decision != player_2_decision:
        rps_match = True
        slow_type("Since the two of you have chosen different numbers, we will be having a rock-paper-scissors match to know which number we will be choosing.", 0.05)
        slow_type("R - Rock\nP - Paper\nS - Scissors", 0.05)
        slow_type("Please Enter Your Preffered Weapon", 0.05)
        while True:
            weapons = ['s', 'r', 'p']
            weapon_names = ["Scissors", "Rock", "Paper"]
            while True:
                player_1_weapon = str(input(f"{player_1.name}: ")).lower()
                if player_1_weapon not in weapons:
                    slow_type("Invalid Input. Please enter only between the given selection", 0.05)
                    continue 
                else:
                    print("\033[F\033[K", end = "")
                    break 
            while True:
                player_2_weapon = str(input(f"{player_2.name}: ")).lower()
                if player_2_weapon not in weapons:
                    slow_type("Invalid Input. Please enter only between the given selection", 0.05)
                    continue 
                else:
                    print("\033[F\033[K", end = "")
                    break

            if (player_1_weapon == 'r' and player_2_weapon == "s") or (player_1_weapon == 's' and player_2_weapon == "p") or (player_1_weapon == 'p' and player_2_weapon == "r"):
                slow_type(f"{player_1.name}'s {weapon_names[weapons.index(player_1_weapon)]} beats {player_2.name}'s {weapon_names[weapons.index(player_2_weapon)]}. Therefore the pokemon battle will follow {player_1_decision} pokemons per trainer", 0.05)
                number_of_pokemon = int(player_1_decision)
                winner = player_1
                loser = player_2
                break
            elif player_1_weapon == player_2_weapon:
                slow_type(f"Both {player_1.name} and {player_2.name} picked {weapon_names[weapons.index(player_1_weapon)]}. Recommencing the match...", 0.05)
                continue
            else:
                slow_type(f"{player_2.name}'s {weapon_names[weapons.index(player_2_weapon)]} beats {player_1.name}'s {weapon_names[weapons.index(player_1_weapon)]}. Therefore the pokemon battle will follow {player_2_decision} pokemons per trainer", 0.05)
                number_of_pokemon = int(player_2_decision)
                winner = player_2
                loser = player_1
                break

    else:
        number_of_pokemon = int(player_1_decision)
        slow_type(f"The pokemon battle will follow {player_1_decision} number of pokemons per trainer.")

    slow_type("Next that we need to decide is who gets first to choose their pokemon. Now we are commencing a coin toss. Choose your preffered coin side", 0.05)
    slow_type("H - Head\nT - Tail")
    if rps_match:
        slow_type(f"Since {loser.name} lost the Rock-Paper-Scissor match, they will have the privilege to choose the side they are on for this coin flip.", 0.05)
        chooser = loser
        other_player = winner
    else:
        slow_type(f"For this match, the one who will have the privilege to pick a coin side will be randomly selected.")
        player_name_list = numpy.array([player_1, player_2], dtype=object)
        for _ in range(random.randint(15, 30)):
            chooser = random.choice(player_name_list) 
            print(f"{chooser.name}")
            time.sleep(0.2)
            print("\033[F\033[K", end= "")
        print(f"{chooser.name}")
        slow_type(f"The player who will choose a coin side is {chooser.name}")
        other_player = player_1 if chooser == player_2 else player_2
    while True:
        chooser_coin = str(input(f"{chooser.name}: ")).lower()
        if chooser_coin not in ['h', 't']:
            slow_type("Please only choose between 'h' (Head) or 't' (Tail)")
            continue
        coin_side_list = numpy.array(["Head", "Tail"], "U4")
        slow_type("Coin flip result is...", 0.5, True)
        for _ in range(random.randint(15,30)):
            print(f"Coin flip result is... {random.choice(coin_side_list)}")
            time.sleep(0.1)
            print("\033[F\033[K", end= "")
        coin_flip_result = random.choice(coin_side_list)
        print(f"Coin flip result is... {coin_flip_result}")
        if chooser_coin == coin_flip_result[0].lower():
            slow_type(f"{chooser.name} won. Therefore they will have the privilege to choose first in the roster of pokemons, followed by {other_player.name}.", 0.5)
            slow_type(f"We will now proceed to pokemon pickings! We will have {chooser.name} then followed by {other_player.name}.")
            player_turn_array = numpy.array([chooser, other_player], dtype= object)
            break
        else:
            slow_type(f"{chooser.name} lost. Therefore {other_player.name} will have the privilege to choose first in the roster of pokemons, followed by {chooser.name}.", 0.5)
            slow_type(f"We will now proceed to pokemon pickings! We will have {other_player.name} then followed by {chooser.name}.")
            player_turn_array = numpy.array([other_player, chooser], dtype= object)
            break
    chosen_pokemons = []
    for turn_number in range(number_of_pokemon*2):
        while True:
            current_index = turn_number % len(player_turn_array)
            current_player = player_turn_array[current_index]
            show_pokemon_table(chosen_pokemons)
            print(f"{current_player.name}'s Remaining Points: {current_player.points}")
            current_player_pokemon_choice = str(input(f"{current_player.name}: ")).title()
            if current_player_pokemon_choice not in pokemon_array["name"]:
                slow_type(f"{current_player_pokemon_choice} is currently not found in the Pokemon Index. Please select only from the available pokemon in the table", 0.5)
                continue
            elif (current_player_pokemon_choice not in current_player.pokemon_name_array and current_player_pokemon_choice not in player_turn_array[0 if current_index == 1 else 1].pokemon_name_array) and (current_player.points - pokemon_array[pokemon_array["name"] == current_player_pokemon_choice]["cost"] >= 0):
                individual_values = pokemon_array[pokemon_array["name"] == current_player_pokemon_choice]
                individual_header = [name.replace("_", " ").title() for name in pokemon_dtype.names]
                individual_table = tabulate.tabulate(individual_values, individual_header, tablefmt= "pretty")
                print(individual_table)
                slow_type(f"Are you sure you want to add {current_player_pokemon_choice} to your roster?\nYour Remaining Points If You Proceed: {(current_player.points - pokemon_array[pokemon_array["name"] == current_player_pokemon_choice]["cost"])[0]}\nEnter 'Yes' if you want to proceed\nEnter any key if you want to go back", 0.5)
                current_player_pokemon_confirm = str(input(f"{current_player.name}: ")).lower()
                if current_player_pokemon_confirm == "yes":
                    slow_type(f"Adding {current_player_pokemon_choice} to {current_player.name}'s inventory", 0.5, True)
                    slow_type("...", 1)
                    current_player.choose_pokemon(Pokemon(pokemon_array[pokemon_array["name"] == current_player_pokemon_choice]))
                    current_player.points = (current_player.points - pokemon_array[pokemon_array["name"] == current_player_pokemon_choice]["cost"])[0]
                    chosen_pokemons.append(current_player_pokemon_choice)
                    break
                else:
                    continue
            elif (current_player_pokemon_choice in chooser.pokemon_name_array or current_player_pokemon_choice in player_turn_array[0 if current_index == 1 else 1].pokemon_name_array):
                if current_player_pokemon_choice in current_player.pokemon_name_array:
                    slow_type(f"You already have {current_player_pokemon_choice} in your roster. Please select a new one.")
                    continue
                if current_player_pokemon_choice in player_turn_array[0 if current_index == 1 else 1].pokemon_name_array:
                    slow_type(f"{player_turn_array[0 if current_index == 1 else 1].name} already owns {current_player_pokemon_choice}. Please select a new one.")
                    continue
            elif current_player.points - pokemon_array[pokemon_array["name"] == current_player_pokemon_choice]["cost"] < 0:
                slow_type("Insufficient points. Please select a pokemon within your remaining points", 0.5)
                continue
    slow_type(f"Now selecting the map for this battle...")
    for _ in range(random.randint(15,30)):
        print(f"{random.choice(map_names)}")
        time.sleep(0.1)
        print("\033[F\033[K", end= "")
    battle_map = random.choice(map_names)
    print(battle_map)
    slow_type(f"Map for this battle: {battle_map} ({'+' if map_effects[numpy.where(map_names == battle_map)][0][0] > 0 else ''}{map_effects[numpy.where(map_names == battle_map)][0][0]*100:.0f}% on Potions, {'+' if map_effects[numpy.where(map_names == battle_map)][0][1] >= 0 else ''}{map_effects[numpy.where(map_names == battle_map)][0][1]*100:.0f}% on Poisons)")
    potion_buff = map_effects[numpy.where(map_names == battle_map)][0][0]
    poison_buff = map_effects[numpy.where(map_names == battle_map)][0][1]
    slow_type(f"Loading",0.5, True)
    slow_type(f"...", 1)
    match = 0
    while True:
        match += 1
        match_end = False
        all_pokemons_used = all([player_1.all_pokemon_used(), player_2.all_pokemon_used()])
        slow_type("Poke-Matcher will now randomly choose fighters from both players!")
        player_array = numpy.array([player_1, player_2], dtype= object)
        fighting_pokemons = numpy.array([], dtype= "i4")
        for current_player in range(2):
            slow_type(f"From {player_array[current_player].name}'s Pokemon Inventory ...",0.5, False)
            for _ in range(random.randint(15,30)):
                print(random.choice(player_array[current_player].pokemon_name_array))
                time.sleep(0.1)
                print("\033[F\033[K", end = "")
            random_pokemon_name = random.choice(player_array[current_player].pokemon_name_array)
            for pokemon in player_array[current_player].pokemon_array:
                if pokemon.name == random_pokemon_name:
                    fighting_pokemons = numpy.append(fighting_pokemons, pokemon)
            print(fighting_pokemons[current_player].name)
            slow_type(f"{player_array[current_player].name}'s fighter for this match is {fighting_pokemons[current_player].name}!")
        slow_type(f"Match {match}: {fighting_pokemons[0].name} vs. {fighting_pokemons[1].name}")
        for current_player_number in range(2):
            current_player = player_array[current_player_number]
            turnover = False
            current_health_increase = 0
            while True:
                print(f"{current_player.name}'s turn")
                show_pokemon_status(fighting_pokemons[current_player_number].status())
                slow_type("Select an action:")
                print(f"[p] - Pass the Turn \t\t[e] - Equip Potion \t\t{'[h] - History Tab' if match > 1 else ''}\n[u] - Use Poison\t\t", end = "")
                print("[r] - Run / Leave the Battle" if all_pokemons_used else "")
                current_player_choice = str(input(f"{current_player.name}: ")).lower()
                if current_player_choice == 'p':
                    slow_type(f"Are you sure? Proceeding will {'give the turn to the opponent' if current_player_number == 0 else 'now start the match'}.\nEnter 'yes' to proceed\nEnter any key to go back.")
                    confirmation = str(input(f"{current_player.name}: ")).lower()
                    if confirmation == 'yes':
                        turnover = True
                        break
                elif current_player_choice == 'e':
                    if fighting_pokemons[current_player_number].potion > 0:
                        potion_buff_amount = int(20 + (20*potion_buff))
                        potion_power_buff_amount = int(15 +(15*potion_buff))
                        slow_type(f"Using a potion will restore {potion_buff_amount} points into your health and also temporarily increase {fighting_pokemons[current_player_number].name}'s power by {potion_power_buff_amount} for this match. Do you wish to proceed?\nEnter 'yes' to proceed\nEnter any key to go back")
                        confirmation = str(input(f"{current_player.name}: ")).lower()
                        if confirmation == 'yes':
                            slow_type(f"{fighting_pokemons[current_player_number].name} successfully used a potion.")
                            fighting_pokemons[current_player_number].potion -= 1
                            current_player.used_potions += 1
                            fighting_pokemons[current_player_number].heal_amount += potion_buff_amount 
                            fighting_pokemons[current_player_number].powerup_amount += potion_power_buff_amount
                            
                    else:
                        slow_type(f"{fighting_pokemons[current_player_number].name}'s does not have any potions left.")
                elif current_player_choice == 'u':
                    if fighting_pokemons[current_player_number].poisons > 0:
                        poison_buff_amount = int(20 + (20*poison_buff))
                        poison_power_debuff_amount = int(10 + (10*poison_buff))
                        slow_type(f"Using a poison will instantly negate {poison_buff_amount} points into the opponent's pokemon health and temporarily lower their power by {poison_power_debuff_amount}. Do you wish to proceed?\nEnter 'yes' to proceed\nEnter any key to go back")
                        confirmation = str(input(f"{current_player.name}: ")).lower()
                        if confirmation == 'yes':
                            slow_type(f"{fighting_pokemons[current_player_number].name} successfully applied poison to its attack.")
                            fighting_pokemons[current_player_number].poisons -= 1
                            current_player.used_poisons += 1
                    else:
                        slow_type(f"{fighting_pokemons[current_player_number].name}'s does not have any poisons left.")
                else:
                    if current_player_choice == 'r' and all_pokemons_used:
                        slow_type(f"Running away or leaving will cause the match to end immediately. Are you sure?\nEnter 'yes' if you want to proceed\nEnter any key to go back")
                        confirmation = str(input(f"{current_player.name}: ")).lower()
                        if confirmation == 'yes':
                            match_end = True
                            turnover = True
                            break
                    elif current_player_choice == 'h' and match > 1:
                        while True:
                            show_history(history_values, player_array[0].name, player_array[1].name)
                            input(f"Enter any key to continue\n{current_player.name}: ")
                            break
                    else:
                        slow_type(f"Invalid input. Please select a valid option above.")
                if turnover:
                    for _ in range(30):
                        print()
                    break
            if match_end:
                end = True
                break
                
     
        
        if end:
            break
        for turn in range(2):
           if player_array[turn].used_potions > 0:
               slow_type(f"{fighting_pokemons[turn].name} has used {player_array[turn].used_potions} potion(s). Making them heal a total of {potion_buff_amount * player_array[turn].used_potions} Health and temporarily gain {potion_power_buff_amount * player_array[turn].used_potions} power.")
               for _ in range(potion_buff_amount * player_array[turn].used_potions):
                    fighting_pokemons[turn].after_health += 1
                    print(f"{fighting_pokemons[turn].name}'s Health: {fighting_pokemons[turn].after_health}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
               print(f"{fighting_pokemons[turn].name}'s Health: {fighting_pokemons[turn].after_health}")
               for _ in range(potion_power_buff_amount * player_array[turn].used_potions):
                    fighting_pokemons[turn].temporary_power += 1
                    print(f"{fighting_pokemons[turn].name}'s Power: {fighting_pokemons[turn].temporary_power}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
               print(f"{fighting_pokemons[turn].name}'s Power: {fighting_pokemons[turn].temporary_power}")
               player_array[turn].used_potions = 0
               fighting_pokemons[turn].heal_amount = 0
               fighting_pokemons[turn].powerup_amount = 0
               slow_type(f"{fighting_pokemons[turn].name}'s new total status:\nHealth: {fighting_pokemons[turn].after_health}\nTemporary Power: {fighting_pokemons[turn].temporary_power}")
        for turn in range(2):
           if player_array[turn].used_poisons > 0:
               slow_type(f"{fighting_pokemons[turn].name} has used {player_array[turn].used_poisons} poison(s). Making {fighting_pokemons[0 if turn == 1 else 1].name} lose {poison_buff_amount * player_array[turn].used_poisons} Health, and temporarily lose {poison_power_debuff_amount * player_array[turn].used_poisons} power.")
               for _ in range(poison_buff_amount * player_array[turn].used_poisons):
                    fighting_pokemons[0 if turn == 1 else 1].after_health -= 1
                    print(f"{fighting_pokemons[0 if turn == 1 else 1].name}'s Health: {fighting_pokemons[0 if turn == 1 else 1].after_health}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
                    if fighting_pokemons[0 if turn == 1 else 1].after_health == 0:
                        break
               print(f"{fighting_pokemons[0 if turn == 1 else 1].name}'s Health: {fighting_pokemons[0 if turn == 1 else 1].after_health}")
               for _ in range(poison_power_debuff_amount * player_array[turn].used_poisons):
                    fighting_pokemons[0 if turn == 1 else 1].temporary_power -= 1
                    print(f"{fighting_pokemons[0 if turn == 1 else 1].name}'s Power: {fighting_pokemons[0 if turn == 1 else 1].temporary_power}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
               print(f"{fighting_pokemons[0 if turn == 1 else 1].name}'s Power: {fighting_pokemons[0 if turn == 1 else 1].temporary_power}")
               player_array[turn].used_poisons = 0
               slow_type(f"{fighting_pokemons[0 if turn == 1 else 1].name}'s new total status:\nHealth: {fighting_pokemons[0 if turn == 1 else 1].after_health}\nTemporary Power: {fighting_pokemons[0 if turn == 1 else 1].temporary_power}")
        slow_type(f"\nWe will now commence the match!")
        if (fighting_pokemons[0].element in fighting_pokemons[1].weakness) or (fighting_pokemons[0].element in fighting_pokemons[1].strength):
            slow_type("Element Interaction Found!")
            slow_type(f"{fighting_pokemons[0].name if fighting_pokemons[0].element in fighting_pokemons[1].weakness else fighting_pokemons[1].name}'s element ({fighting_pokemons[0].element if fighting_pokemons[0].element in fighting_pokemons[1].weakness else fighting_pokemons[1].element}) is effective against {fighting_pokemons[1].name if fighting_pokemons[0].element in fighting_pokemons[1].weakness else fighting_pokemons[0].name}'s element ({fighting_pokemons[1].element if fighting_pokemons[0].element in fighting_pokemons[1].weakness else fighting_pokemons[0].element}). Causing {fighting_pokemons[0].name if fighting_pokemons[0].element in fighting_pokemons[1].weakness else fighting_pokemons[1].name} to either boost own damage or reduce receiving damage by 50%. In addition, {fighting_pokemons[0].name if fighting_pokemons[0].element in fighting_pokemons[1].weakness else fighting_pokemons[1].name} will have higher chance to increase it's own power.")

            slow_type(f"Due to environment features of the battlefield, {fighting_pokemons[0].name} and {fighting_pokemons[1].name} have some changes to their temporary power.")
            if fighting_pokemons[0].element in fighting_pokemons[1].weakness:
                stronger_buff = random.randint(0, fighting_pokemons[1].power + 10)
                weaker_buff = random.randint(-5, fighting_pokemons[0].power)
                for _ in range(stronger_buff):
                    fighting_pokemons[0].temporary_power += 1
                    print(f"{fighting_pokemons[0].name}'s Power: {fighting_pokemons[0].temporary_power}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
                print(f"{fighting_pokemons[0].name}'s Final Power: {fighting_pokemons[0].temporary_power}")
                for _ in range(weaker_buff):
                    if weaker_buff < 0 :
                        fighting_pokemons[1].temporary_power += 1
                    else:
                        fighting_pokemons[1].temporary_power += 1
                    print(f"{fighting_pokemons[1].name}'s Power: {fighting_pokemons[1].temporary_power}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
                print(f"{fighting_pokemons[1].name}'s Final Power: {fighting_pokemons[1].temporary_power}")
                fighting_pokemons[0].damage_boost = 0.5
            else:
                stronger_buff = random.randint(0, fighting_pokemons[0].power + 10)
                weaker_buff = random.randint(-5, fighting_pokemons[1].power)
                for _ in range(stronger_buff):
                    fighting_pokemons[1].temporary_power += 1
                    print(f"{fighting_pokemons[1].name}'s Power: {fighting_pokemons[1].temporary_power}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
                print(f"{fighting_pokemons[1].name}'s Final Power: {fighting_pokemons[1].temporary_power}")
                for _ in range(weaker_buff):
                    if weaker_buff < 0 :
                        fighting_pokemons[0].temporary_power += 1
                    else:
                        fighting_pokemons[0].temporary_power += 1
                    print(f"{fighting_pokemons[0].name}'s Power: {fighting_pokemons[0].temporary_power}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
                print(f"{fighting_pokemons[0].name}'s Final Power: {fighting_pokemons[0].temporary_power}")
        else:
            slow_type(f"Due to environment features of the battlefield, {fighting_pokemons[0].name} and {fighting_pokemons[1].name} have some changes to their temporary power.")
            for turn in range(2):
                for _ in range(random.randint(0, fighting_pokemons[1 if turn == 0 else 0].power)):
                    fighting_pokemons[turn].temporary_power += 1
                    print(f"{fighting_pokemons[turn].name}'s Power: {fighting_pokemons[turn].temporary_power}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
                print(f"{fighting_pokemons[turn].name}'s Final Power: {fighting_pokemons[turn].temporary_power}")
        if fighting_pokemons[0].temporary_power == fighting_pokemons[1].temporary_power:
            slow_type(f"After facing each other, both pokemons passed out, both receiving damage.")
            for turn in range(2):
                slow_type(f"{fighting_pokemons[turn].name}'s Health: {fighting_pokemons[turn].after_health} - {10 - int(fighting_pokemons[turn].damage_boost * 10)}{' (-50% due to elemental boost)' if fighting_pokemons[turn].damage_boost > 0 else ''}")
                for _ in range(10 - int(fighting_pokemons[turn].damage_boost * 10)):
                    fighting_pokemons[turn].after_health -= 1
                    print(f"{fighting_pokemons[turn].name}'s Health: {fighting_pokemons[turn].after_health}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
                    if fighting_pokemons[turn].after_health <= 0:
                        fighting_pokemons[turn].after_health = 0
                        break
                print(f"{fighting_pokemons[turn].name}'s Health: {fighting_pokemons[turn].after_health}")
            slow_type("Battle is a tie.")
        else:
            slow_type(f"After facing each other, {f"{fighting_pokemons[0].name if fighting_pokemons[0].temporary_power > fighting_pokemons[1].temporary_power else fighting_pokemons[1].name}'s power overwhelmed {fighting_pokemons[1].name if fighting_pokemons[0].temporary_power > fighting_pokemons[1].temporary_power else fighting_pokemons[0].name}'s power. Leaving {fighting_pokemons[1].name if fighting_pokemons[0].temporary_power > fighting_pokemons[1].temporary_power else fighting_pokemons[0].name} vulnerable for an attack."}")
            if fighting_pokemons[0].temporary_power > fighting_pokemons[1].temporary_power:
                damage = 20 + int(f'{10*fighting_pokemons[0].damage_boost if fighting_pokemons[0].damage_boost >= fighting_pokemons[1].damage_boost else -10*fighting_pokemons[1].damage_boost:.0f}')
                slow_type(f"{fighting_pokemons[0].name} landed an attack, and dealt {damage} to {fighting_pokemons[1].name}'s health.")
                for _ in range(damage):
                    fighting_pokemons[1].after_health -= 1
                    print(f"{fighting_pokemons[1].name}'s Health: {fighting_pokemons[1].after_health}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
                    if fighting_pokemons[1].after_health <= 0:
                        break
                print(f"{fighting_pokemons[1].name}'s Remaining Health: {fighting_pokemons[1].after_health}")
                for _ in range(5):
                    fighting_pokemons[0].after_health += 1
                    print(f"{fighting_pokemons[0].name}'s Health: {fighting_pokemons[0].after_health}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
                print(f"{fighting_pokemons[0].name}'s Remaining Health: {fighting_pokemons[0].after_health}")
                slow_type(f"{player_array[0].name} wins this battle!")
                player_array[0].number_of_wins += 1
                slow_type(f"Match {match}: {player_array[0].name} wins.")
                
            elif fighting_pokemons[0].temporary_power < fighting_pokemons[1].temporary_power:
                damage = 20 + int(f'{10*fighting_pokemons[1].damage_boost if fighting_pokemons[1].damage_boost >= fighting_pokemons[0].damage_boost else 10-(10*fighting_pokemons[0].damage_boost):.0f}')
                slow_type(f"{fighting_pokemons[1].name} landed an attack, and dealt {damage} to {fighting_pokemons[0].name}'s health.")
                for _ in range(damage):
                    fighting_pokemons[0].after_health -= 1
                    print(f"{fighting_pokemons[0].name}'s Health: {fighting_pokemons[0].after_health}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
                    if fighting_pokemons[0].after_health <= 0:
                        fighting_pokemons[0].after_health = 0
                        break
                print(f"{fighting_pokemons[0].name}'s Remaining Health: {fighting_pokemons[0].after_health}")
                for _ in range(5):
                    fighting_pokemons[1].after_health += 1
                    print(f"{fighting_pokemons[1].name}'s Health: {fighting_pokemons[1].after_health}")
                    time.sleep(0.2)
                    print("\033[F\033[K", end = "")
                print(f"{fighting_pokemons[1].name}'s Remaining Health: {fighting_pokemons[1].after_health}")
                
                slow_type(f"{player_array[1].name} wins this battle!")
                player_array[1].number_of_wins += 1

                slow_type(f"Match {match}: {player_array[1].name} wins.")
            
        slow_type("Due to fatigue, both pokemons have lost 2 points of health")
        for turn in range(2):
            for _ in range(2):
                fighting_pokemons[turn].after_health -= 1
                if fighting_pokemons[turn].after_health < 0:
                    fighting_pokemons[turn].after_health = 0
                    break
                print(f"{fighting_pokemons[turn].name}'s Health: {fighting_pokemons[0].after_health}")
                time.sleep(0.2)
                print("\033[F\033[K", end = "")
            print(f"{fighting_pokemons[turn].name}'s Remaining Health: {fighting_pokemons[turn].after_health}")
        history_values.append([match, f"{fighting_pokemons[0].name}\nvs.\n{fighting_pokemons[1].name}", fighting_pokemons[0].health, fighting_pokemons[1].health,fighting_pokemons[0].temporary_power, fighting_pokemons[1].temporary_power, f"{f'{player_array[0].name} Won' if fighting_pokemons[0].temporary_power > fighting_pokemons[1].temporary_power else f'{player_array[1].name} Won' if fighting_pokemons[0].temporary_power < fighting_pokemons[1].temporary_power else 'Tie' }", fighting_pokemons[0].after_health, fighting_pokemons[1].after_health])
        for turn in range(2):    
            fighting_pokemons[turn].fight()
            fighting_pokemons[turn].temporary_power = fighting_pokemons[turn].power
            fighting_pokemons[turn].health = fighting_pokemons[turn].after_health
            print(player_array[turn].total_health())
            if fighting_pokemons[turn].health == 0:
                player_array[turn].pokemon_died(fighting_pokemons[turn].name)
            if player_array[turn].total_health() == 0:
                slow_type(f"{player_array[turn].name} has no remaining pokemon in their inventory.\nEnd of battle.")
                match_end = True
        
        if match_end:
            break
            
        slow_type(f"Recommencing battle ...\n\n")
    
    slow_type("Battle Summary: ")
    show_history(history_values, player_1.name, player_2.name)
    print()
    show_summary(player_1, player_2)
    slow_type(f"No. of {player_1.name}'s win: {player_1.number_of_wins}")
    slow_type(f"No. of {player_2.name}'s win: {player_2.number_of_wins}")
    slow_type(f"Overall Winner (based on Remaining Total Health): {player_1.name if player_1.total_health() > player_2.total_health() else player_2.name}")
    restart_game = False
    end = True
    while True:
        slow_type("Select preferred action")
        ending_choice = str(input(f'[q] - Queue a match again\t\t[x] - Close the program\nUser: ')).lower()
        if ending_choice == 'q':
            slow_type("Proceeding will restart the whole game, erasing your progress of this match.")
            slow_type(f"Press [c] to continue\nPress any key if otherwise")
            confirmation = str(input("User: ")).lower()
            if confirmation == 'c':
                restart_game = True
                break
            else:
                continue
        if ending_choice == 'x':
            end = True
            slow_type("Thank you for playing! Hope to see you again!")
            break
        else:
            slow_type("Invalid choice. Please select only from options above!")
            continue
    if restart_game:
        continue
    if end:
        break
                
            



        
        
        




        
    





    