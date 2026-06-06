from game.settings import GAME_LEVELS
from game.models import Player, Computer
from game.exceptions import InvalidInputError, InvalidRollError
from game.score import save_result
import datetime as dtm




def start_game():
    """Starts the dice game and controls the main game process."""
    data = dtm.datetime.now()
    print("Game started")
    while True:
        try:
            name = input("Enter your name: ")
            if name == "":
                raise InvalidInputError("The string cannot be empty!")
            else:
                break
        except InvalidInputError as e:
            print(e)

    while True:
        try:
            round_choice = input("Select game level:\n1 - Short (5 rounds) \n2 - Medium (8 rounds) \n3 - Long (10 rounds) \nYour choice: ")
            if round_choice not in GAME_LEVELS:
                raise InvalidInputError("Incorrect choice! Try again.")
            else:
                rounds = GAME_LEVELS[round_choice]
                break
        except InvalidInputError as e:
            print(e)

    player = Player(name)
    computer = Computer()
    for i in range(1, rounds + 1):
        while True:
            try:
                enter = input("Press Enter")
                if enter != "":
                    raise InvalidRollError("The throw was not made!!! Press ""Enter"" to throw again.")
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
                break
            except InvalidRollError as e:
                print(e)
    print("---------------------------------")
    print("Game finished!")
    print(f"Date: {data}")
    print(f"Name: {name}")
    print(f"Number of rounds: {rounds}")
    print(f"Final score: {player.score}")
    print("---------------------------------")
    save_result(name, rounds, player.score)

        
                

            
            
            

        

