# НЕ ЗАБУДЬ ЗА """"""
from game.settings import GAME_LEVELS
from game.models import Player
from game.models import Computer
from game.exceptions import InvalidInputError
from game.exceptions import InvalidRollError



def start_game():
    print("Game started")
    try:
        while True:
            name = input("Enter your name: ")
            if name == "":
                raise InvalidInputError("The string cannot be empty!")
            else:
                break
    except InvalidInputError as e:
        print(e)
    while True:
        round_choice = input("Select game level: \n1 - Short (5 rounds) \n2 - Medium (8 rounds) \n3 - Long (10rounds) \nYour choice: ")
        if round_choice in GAME_LEVELS:
            rounds = GAME_LEVELS[round_choice]
            break
        else:
            print("Incorrect choice! Try again.")
    player = Player(name)
    computer = Computer()
    for i in range(1, rounds + 1):
        enter = input("Press Enter")
        if enter != "":
            print("The throw was not made!!! Press ""Enter"" to throw again.")
        else:
            player_roll = player.roll_dice()
            computer_roll = computer.roll_dice()
            while player_roll == computer_roll:
                player_roll = player.roll_dice()
                computer_roll = computer.roll_dice()
            if player_roll > computer_roll:
                difference = player_roll - computer_roll
                player.score = player.score + difference
            elif computer_roll > player_roll:
                difference = computer_roll - player_roll
                player.score = player.score - difference
            result = f"Round {i}: \nYou rolled the dice: 🎲 {player_roll} \nThe computer rolled the dice: 🎲 {computer_roll} \nDifference: {difference} points"
            print(result)

                
                

            
            
            

        

