import random
import time
import os

PLAY = True
TURN = 1

class Pokemon:
  def __init__(self, id, name, type, atk, dfn, spd, level):
    self.id = id
    self.name = name
    self.type = type
    self.atk = round(atk * (1.02 + (level / 100)))
    self.dfn = round(dfn * (1.02 + (level / 100)))
    self.spd = round(spd * (1.02 + (level / 100)))
    self.level = level
    self.hit_points = round((level * 10) * (1.02 + (level / 100)))
    self.max_hit_points = round((level * 10) * (1.02 + (level / 100)))
    self.has_fainted = False

  def __str__(self):
    # User readable string representation of the object
    # Removes stats if fainted
    if self.has_fainted:
      return "(~{id}~) {name}. FAINTED!".format(id = self.id, name = self.name)
    # Prints full info
    else:
      return "(~{id}~) {name}. A level {level} {type} type Pokemon. It's stats are {atk} Attack, {dfn} Defense, {spd} Speed and {hit_points} Hit Points".format(id = self.id, name = self.name, level = self.level, type = self.type, atk = self.atk, dfn = self.dfn, spd = self.spd, hit_points=self.hit_points)

  def attack(self, defending_pokemon):
    # Damage formula
    damage = round((self.level)*(self.atk/defending_pokemon.dfn))*5
    # Regular damage based on type
    if (self.type == defending_pokemon.type):
      print("{attacker_name} attacks {defender_name} for {damage} damage.".format(attacker_name = self.name, defender_name = defending_pokemon.name, damage = damage))
      defending_pokemon.lose_hit_points(damage)
    # Reduced damage based on type
    elif (self.type == "Fire" and defending_pokemon.type == "Water") or (self.type == "Water" and defending_pokemon.type == "Grass") or (self.type == "Grass" and defending_pokemon.type == "Fire"):
      print("{attacker_name} attacks {defender_name} for {damage} damage.".format(attacker_name = self.name, defender_name = defending_pokemon.name, damage = round(damage * 0.5)))
      print("It's not very effective")
      defending_pokemon.lose_hit_points(round(damage * 0.5))
    # Boosted damage based on type
    elif (self.type == "Fire" and defending_pokemon.type == "Grass") or (self.type == "Water" and defending_pokemon.type == "Fire") or (self.type == "Grass" and defending_pokemon.type == "Water"):
      print("{attacker_name} attacks {defender_name} for {damage} damage.".format(attacker_name = self.name, defender_name = defending_pokemon.name, damage = damage * 2))
      print("It's super effective")
      defending_pokemon.lose_hit_points(damage * 2)

  def lose_hit_points(self, amount):
    self.hit_points -= amount
    if self.hit_points <= 0:
      #Makes the Pokemon faint if Hit Points below zero
      self.has_fainted = True
      print("(~{id}~) {name} has fainted!".format(id = self.id, name = self.name))
    else:
      print("(~{id}~) {name} now has {hit_points} Hit Points.".format(id = self.id, name = self.name, hit_points = self.hit_points))

  def gain_hit_points(self, amount):
    self.hit_points += amount
    # Checks Hit Points don't exceed maximum
    if self.hit_points > self.max_hit_points:
      self.hit_points = self.max_hit_points
    print("(~{id}~) {name} now has {hit_points} Hit Points.".format(id = self.id, name = self.name, hit_points = self.hit_points))

class Trainer:
  def __init__(self, name, pokemon_list, num_potions,):
    self.name = name
    self.pokemons = pokemon_list
    self.potions = num_potions
    self.current_pokemon = 0

  def __str__(self):
    # User readable string representation of the object
    print("{name}'s team is".format(name = self.name))
    for pokemon in self.pokemons:
      print(pokemon)
    return "{name}'s active Pokemon is (~{id}~) {pokemon_name}".format(name = self.name, id = self.pokemons[self.current_pokemon].id, pokemon_name = self.pokemons[self.current_pokemon].name)

  def switch_pokemon(self):
    # Gets the user to select the new Pokemon
    pokemon_selection = int(input("\nSelect a Pokemon: (Type 1, 2 or 3)\n>>"))
    # Converts the user input to the correct list indicies
    pokemon_selection-=1
    # Prevents switching to a Pokemon that has fainted
    if self.pokemons[pokemon_selection].has_fainted:
      print("(~{id}~) {name} has fainted and cannot be selected".format(id = self.pokemons[pokemon_selection].id, name = self.pokemons[pokemon_selection].name))
    # Prevents switching to the active Pokemon
    elif pokemon_selection == self.current_pokemon:
      print("(~{id}~) {name} is already active".format(id = self.pokemons[pokemon_selection].id, name = self.pokemons[pokemon_selection].name))
    # Switches the Pokemon
    else:
      self.current_pokemon = pokemon_selection
      print("I Cho-cho-choose you {name}!".format(name = self.pokemons[self.current_pokemon].name))

  def use_potion(self):
    # Checks a potion is available
    if self.potions > 0:
      print("\nYou used a potion on (~{id}~) {name}.".format(id = self.pokemons[self.current_pokemon].id, name = self.pokemons[self.current_pokemon].name))
      # A potion is consumed and restores 50 Hit Points
      self.pokemons[self.current_pokemon].gain_hit_points(50)
      self.potions -= 1
    else:
      print("\nYou don't have any potions")

# Three subclasses of Pokemon
class Charmander(Pokemon):
  def __init__(self, id, level):
      super().__init__(id, "Charmander", "Fire", 52, 43, 65, level)

class Squirtle(Pokemon):
  def __init__(self, id, level):
      super().__init__(id, "Squirtle", "Water", 48, 65, 43, level)

class Bulbasaur(Pokemon):
  def __init__(self, id, level):
      super().__init__(id, "Bulbasaur", "Grass", 49, 49, 45, level)

def setup_teams(team_size):
  # Creates a list of random Pokemon with random levels representing the trainers teams
  pokemon_list = [None] * (team_size*2)
  pokemon_id = 1
  for i in range(team_size*2):
    #Sets the Pokemon for each player to have consecutive ID's from 1
    if pokemon_id > team_size:
      pokemon_id = 1
    #Chooses a Pokemon type at random and gives it a random level
    pick_pokemon_type = random.randint(1, 3)
    if pick_pokemon_type == 1:
      pokemon_list[i] = Charmander([pokemon_id], random.randint(1, 10))
      pokemon_id+=1
    elif pick_pokemon_type == 2:
      pokemon_list[i] = Squirtle([pokemon_id], random.randint(1, 10))
      pokemon_id+=1
    elif pick_pokemon_type == 3:
      pokemon_list[i] = Bulbasaur([pokemon_id], random.randint(1, 10))
      pokemon_id+=1
  return pokemon_list

def setup_trainers(pokemon_list):
  # Creates two trainers and assigns their three Pokemon and 1-3 potions
  trainer_one = Trainer("Ash", [pokemon_list[0], pokemon_list[1], pokemon_list[2]], random.randint(1, 3))
  trainer_two = Trainer("Misty", [pokemon_list[3], pokemon_list[4], pokemon_list[5]], random.randint(1, 3))
  return trainer_one, trainer_two

def check_for_winner(attacker):
  # Flags the winner if all Pokemon have fainted
  if (attacker.pokemons[0].has_fainted == True and attacker.pokemons[1].has_fainted == True and attacker.pokemons[2].has_fainted == True):
    # If player one has lost
    if attacker == trainer_one:
      gfx(5)
      return True
    # if player two has lost
    else:
      gfx(4)
      return True
  else:
    return False

def check_turn(TURN):
  # Checks whose TURN it is
  if TURN % 2 == 1:
    attacker = trainer_one
    defender = trainer_two
  else:
    attacker = trainer_two
    defender = trainer_one
  return attacker, defender

def display_teams(attacker, defender):
  # Displays the current teams and their stats
  # Displays the active player
  if attacker == trainer_one:
    gfx(2)
  else:
    gfx(3)
  print("\n", attacker, "\n")
  # Displays the defender with limited information
  print(" {name}'s team is".format(name = defender.name))
  for pokemon in defender.pokemons:
    if pokemon.has_fainted == True:
      print("(~{id}~) {pokemon_name} - FAINTED!".format(id = pokemon.id, pokemon_name = pokemon.name))
    else:
      print("(~{id}~) {pokemon_name} - Level {level}".format(id = pokemon.id, pokemon_name = pokemon.name, level = pokemon.level))
  print("{name}'s active Pokemon is (~{id}~) {pokemon_name}\n".format(name = defender.name, id = defender.pokemons[defender.current_pokemon].id, pokemon_name = defender.pokemons[defender.current_pokemon].name))

def gfx(selection):
  if selection == 1:
    print(r"""
                                        ,'\
        _.----.        ____         ,'  _\   ___    ___     ____
    _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
    \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
     \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
       \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
        \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
         \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
          \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
           \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
            \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                    `'                            '-._|
    """)
  elif selection == 2:
    print(r"""
    :::'###:::::'######::'##::::'##:'####::'######:::::'########:'##::::'##:'########::'##::: ##:
    ::'## ##:::'##... ##: ##:::: ##: ####:'##... ##::::... ##..:: ##:::: ##: ##.... ##: ###:: ##:
    :'##:. ##:: ##:::..:: ##:::: ##:. ##:: ##:::..:::::::: ##:::: ##:::: ##: ##:::: ##: ####: ##:
    '##:::. ##:. ######:: #########:'##:::. ######:::::::: ##:::: ##:::: ##: ########:: ## ## ##:
     #########::..... ##: ##.... ##:..:::::..... ##::::::: ##:::: ##:::: ##: ##.. ##::: ##. ####:
     ##.... ##:'##::: ##: ##:::: ##:::::::'##::: ##::::::: ##:::: ##:::: ##: ##::. ##:: ##:. ###:
     ##:::: ##:. ######:: ##:::: ##:::::::. ######:::::::: ##::::. #######:: ##:::. ##: ##::. ##:
    ..:::::..:::......:::..:::::..:::::::::......:::::::::..::::::.......:::..:::::..::..::::..::
    """)
  elif selection == 3:
    print(r"""
    '##::::'##:'####::'######::'########:'##:::'##:'####::'######:::::'########:'##::::'##:'########::'##::: ##:
     ###::'###:. ##::'##... ##:... ##..::. ##:'##:: ####:'##... ##::::... ##..:: ##:::: ##: ##.... ##: ###:: ##:
     ####'####:: ##:: ##:::..::::: ##:::::. ####:::. ##:: ##:::..:::::::: ##:::: ##:::: ##: ##:::: ##: ####: ##:
     ## ### ##:: ##::. ######::::: ##::::::. ##::::'##:::. ######:::::::: ##:::: ##:::: ##: ########:: ## ## ##:
     ##. #: ##:: ##:::..... ##:::: ##::::::: ##::::..:::::..... ##::::::: ##:::: ##:::: ##: ##.. ##::: ##. ####:
     ##:.:: ##:: ##::'##::: ##:::: ##::::::: ##::::::::::'##::: ##::::::: ##:::: ##:::: ##: ##::. ##:: ##:. ###:
     ##:::: ##:'####:. ######::::: ##::::::: ##::::::::::. ######:::::::: ##::::. #######:: ##:::. ##: ##::. ##:
    ..:::::..::....:::......::::::..::::::::..::::::::::::......:::::::::..::::::.......:::..:::::..::..::::..::  
    """)
  elif selection == 4:
    print(r"""    
     █████╗ ███████╗██╗  ██╗    ██╗    ██╗██╗███╗   ██╗███████╗██╗
    ██╔══██╗██╔════╝██║  ██║    ██║    ██║██║████╗  ██║██╔════╝██║
    ███████║███████╗███████║    ██║ █╗ ██║██║██╔██╗ ██║███████╗██║
    ██╔══██║╚════██║██╔══██║    ██║███╗██║██║██║╚██╗██║╚════██║╚═╝
    ██║  ██║███████║██║  ██║    ╚███╔███╔╝██║██║ ╚████║███████║██╗
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝
    """)
  elif selection == 5:
    print(r"""
    ███╗   ███╗██╗███████╗████████╗██╗   ██╗    ██╗    ██╗██╗███╗   ██╗███████╗██╗
    ████╗ ████║██║██╔════╝╚══██╔══╝╚██╗ ██╔╝    ██║    ██║██║████╗  ██║██╔════╝██║
    ██╔████╔██║██║███████╗   ██║    ╚████╔╝     ██║ █╗ ██║██║██╔██╗ ██║███████╗██║
    ██║╚██╔╝██║██║╚════██║   ██║     ╚██╔╝      ██║███╗██║██║██║╚██╗██║╚════██║╚═╝
    ██║ ╚═╝ ██║██║███████║   ██║      ██║       ╚███╔███╔╝██║██║ ╚████║███████║██╗
    ╚═╝     ╚═╝╚═╝╚══════╝   ╚═╝      ╚═╝        ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝    
    """)

def menu():
  print("Choose an option: (Type 1, 2, 3 or 4)")
  print("[1] Attack")
  print("[2] Switch Pokemon")
  print("[3] Heal Pokemon")
  print("[4] QUIT")

def end_turn():
  # Adds delay to simulate action and clears screen of active players information
  time.sleep(3)
  os.system('cls' if os.name == 'nt' else 'clear')

pokemon_list = setup_teams(3)
trainer_one, trainer_two = setup_trainers(pokemon_list)
# Intro Graphic
gfx(1)

while (PLAY == True):
  attacker, defender = check_turn(TURN)
  if check_for_winner(attacker):
    break
  else:
    display_teams(attacker, defender)
    # Forces the player to switch Pokemon if the current Pokemon has fainted
    if attacker.pokemons[attacker.current_pokemon].has_fainted == True:
      attacker.switch_pokemon()
      end_turn()
    else:
      # Displays the menu
      menu()
      # Gets player to choose an action
      action_choice = input(">>")
      # ATTACK
      if action_choice == "1":
        attacker.pokemons[attacker.current_pokemon].attack(defender.pokemons[defender.current_pokemon])
        TURN+=1
        end_turn()
      # SWITCH POKEMON
      elif action_choice == "2":
        attacker.switch_pokemon()
        TURN+=1
        end_turn()
      # HEAL POKEMON
      elif action_choice == "3":
        attacker.use_potion()
        TURN+=1
        end_turn()
      # QUIT
      elif action_choice == "4":
        PLAY = False
      else:
        input("Invalid selection. Type 1, 2, 3, or 4\n>>")