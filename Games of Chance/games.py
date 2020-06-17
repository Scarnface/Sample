import random
import time

PLAY = True
MONEY = 100

def menu():
  print("You have £{}".format(MONEY))
  print("Choose a game:")
  print("[1] Coin Flip")
  print("[2] High Card")
  print("[3] Cho Han")
  print("[4] Roulette")
  print("[5] QUIT")

def gfx(game_type):
  # Displays a graphic for each game type or game status
  if game_type == "1":
    print(r"""/                       
    ___oooo____________oo______________ooooooo_oo______oooo_ooooooo__
    _oo____oo__ooooo_______oo_ooo______oo______oo_______oo__oo____oo_
    oo________oo___oo__oo__ooo___o_____oooo____oo_______oo__oo____oo_
    oo________oo___oo__oo__oo____o_____oo______oo_______oo__oooooo___
    _oo____oo_oo___oo__oo__oo____o_____oo______oo_______oo__oo_______
    ___oooo____ooooo__oooo_oo____o_____oo______ooooooo_oooo_oo_______
    _________________________________________________________________
    """)
  elif game_type == "2":
    print(r"""/                       
    .------..------..------..------.       .------..------..------..------.
    |H.--. ||I.--. ||G.--. ||H.--. |       |C.--. ||A.--. ||R.--. ||D.--. |
    | :/\: || (\/) || :/\: || :/\: |       | :/\: || (\/) || :(): || :/\: |
    | (__) || :\/: || :\/: || (__) |       | :\/: || :\/: || ()() || (__) |
    | '--'H|| '--'I|| '--'G|| '--'H|       | '--'C|| '--'A|| '--'R|| '--'D|
    `------'`------'`------'`------'       `------'`------'`------'`------'
    """)
  elif game_type == "3":
    print(r"""/                       
         ___      ___      ___           ___      ___      ___   
        /\  \    /\__\    /\  \         /\__\    /\  \    /\__\  
       /::\  \  /:/__/_  /::\  \       /:/__/_  /::\  \  /:| _|_ 
      /:/\:\__\/::\/\__\/:/\:\__\     /::\/\__\/::\:\__\/::|/\__\
      \:\ \/__/\/\::/  /\:\/:/  /     \/\::/  /\/\::/  /\/|::/  /
       \:\__\    /:/  /  \::/  /        /:/  /   /:/  /   |:/  / 
        \/__/    \/__/    \/__/         \/__/    \/__/    \/__/  
    """)
  elif game_type == "4":
    print(r"""/                       
    %%%%%%%%:::'%%%%%%%::'%%::::'%%:'%%:::::::'%%%%%%%%:'%%%%%%%%:'%%%%%%%%:'%%%%%%%%:
    %%.... %%:'%%.... %%: %%:::: %%: %%::::::: %%.....::... %%..::... %%..:: %%.....::
    %%:::: %%: %%:::: %%: %%:::: %%: %%::::::: %%:::::::::: %%::::::: %%:::: %%:::::::
    %%%%%%%%:: %%:::: %%: %%:::: %%: %%::::::: %%%%%%:::::: %%::::::: %%:::: %%%%%%:::
    %%.. %%::: %%:::: %%: %%:::: %%: %%::::::: %%...::::::: %%::::::: %%:::: %%...::::
    %%::. %%:: %%:::: %%: %%:::: %%: %%::::::: %%:::::::::: %%::::::: %%:::: %%:::::::
    %%:::. %%:. %%%%%%%::. %%%%%%%:: %%%%%%%%: %%%%%%%%:::: %%::::::: %%:::: %%%%%%%%:
    ..:::::..:::.......::::.......:::........::........:::::..::::::::..:::::........:
    """)
  elif game_type == "5":
    print(r"""                                                                                      
     @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
    @@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
    !@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  
    !@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  
    !@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   
    !!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
    :!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!   
    :!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  
     ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::  
     :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : :  
    """)
  elif game_type == "6":
    print(r"""/                       
      ______    ______    ______   ______  __    __   ______  
     /      \  /      \  /      \ /      |/  \  /  | /      \ 
    /$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$/ $$  \ $$ |/$$$$$$  |
    $$ |  $$/ $$ |__$$ |$$ \__$$/   $$ |  $$$  \$$ |$$ |  $$ |
    $$ |      $$    $$ |$$      \   $$ |  $$$$  $$ |$$ |  $$ |
    $$ |   __ $$$$$$$$ | $$$$$$  |  $$ |  $$ $$ $$ |$$ |  $$ |
    $$ \__/  |$$ |  $$ |/  \__$$ | _$$ |_ $$ |$$$$ |$$ \__$$ |
    $$    $$/ $$ |  $$ |$$    $$/ / $$   |$$ | $$$ |$$    $$/ 
     $$$$$$/  $$/   $$/  $$$$$$/  $$$$$$/ $$/   $$/  $$$$$$/                                                           
    """)    

def bet_amount():
  bet = int(input("How much will you bet?\n>>"))
  # Checks the bet is greater than zero and not more than the players current balance
  if bet <= 0 or bet > MONEY:
    print("Invalid bet. Please enter an amount between 1 and {}".format(MONEY))
    bet_amount()
  else:
    return bet

def coin_flip(bet):
  guess = input("Choose: Heads OR Tails\n>>").lower()
  print("You chose " + guess.capitalize())
  time.sleep(3)

  # Determines binary heads or tails
  result = random.randint(1,2)
  if result == 1:
    print("\n\nIt's Heads!")
  elif result == 2:
    print("\n\nIt's Tails")

  # Updates player balance and informs them of their win
  if (guess == "heads" and result == 1) or (guess == "tails" and result == 2):
    print("You won £{}!\n\n".format(bet))
    time.sleep(3)
    return bet
  else:
    print("You lost £{}!\n\n".format(bet))
    time.sleep(3)
    return -bet

def high_card(bet):

  # Picks two integers to represent cards
  print("Shuffling the deck.\n\n")
  player = random.randint(1, 10)
  computer = random.randint(1, 10)
  time.sleep(3)
  print("Your card was {}.".format(player))
  print("The computers card was {}.".format(computer))

  # Updates player balance and informs them of their win
  if player > computer:
    print("You won £{}!\n\n".format(bet))
    return bet
  elif player < computer:
    print("You lost £{}!\n\n".format(bet))
    return -bet
  else:
    print("It was a tie!\n\n")
    return 0

def cho_han(bet):
  guess = input("Choose: Odd OR Even\n>>").lower()
  # Rolls two six sided dice and adds the totals together
  print("ShAkInG dIcE!\n\n")
  time.sleep(3)
  dice_1 = random.randint(1, 6)
  dice_2 = random.randint(1, 6)
  total = dice_1 + dice_2
  print("You rolled {}.".format(total))

  # Updates player balance and informs them of their win
  if (guess == "even" and total % 2 == 0) or (guess == "odd" and total % 2 == 1):
    print("You won £{}!\n\n".format(bet))
    return bet
  else:
    print("You lost £{}!\n\n".format(bet))
    return -bet

def roulette(bet):
  guess = input("Choose: Odd OR Even OR Pick a number between 0 and 36\n>>").lower()
  # Picks a random slot on a roulette wheel
  print("Spinning the wheel!\n\n")
  time.sleep(3)
  result = random.randint(0, 36)
  print("The wheel landed on {}.".format(result))

  # Updates player balance and informs them of their win
  if (result != 0 and result % 2 == 0 and guess == "even") or (result != 0 and result % 2 == 1 and guess == "odd"):
    print("You won £{}!\n\n".format(bet))
    return bet
  elif guess == str(result):
    print("You won £{}!\n\n".format(bet*35))
    return bet * 35
  else:
    print("You lost £{}!\n\n".format(bet))
    return -bet

# Intro Graphic
gfx(6)
while PLAY == True:
  # Checks player has money to play
  if MONEY <= 0:
    print("You're broke!")
    gfx("5")
    PLAY = False
    break

  # Displays the menu
  menu()
  # Gets player to choose an action
  game_type = input(">>")
  # COIN FLIP
  if game_type == "1":
    gfx("1")
    bet = bet_amount()
    MONEY += coin_flip(bet)
  # HIGH CARD
  elif game_type == "2":
    gfx("2")
    bet = bet_amount()
    MONEY += high_card(bet)
  # CHO HAN
  elif game_type == "3":
    gfx("3")
    bet = bet_amount()
    MONEY += cho_han(bet)
  # ROULETTE
  elif game_type == "4":
    gfx("4")
    bet = bet_amount()
    MONEY += roulette(bet)
  # QUIT
  elif game_type == "5":
    gfx("5")
    PLAY = False
  else:
    input("Invalid selection. Type 1, 2, 3, 4 or 5\n>>")