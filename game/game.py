from game.settings import GAME_LEVELS
from game.models import Player, Computer
from game.exceptions import InvalidInputError, InvalidRollError
from game.score import ScoreManager
import datetime as dtm

class DiceGame:
    """Starts the dice game and controls the main game process."""
    data = dtm.datetime.now()
    print("Game started")

    def get_player_name(self):
        while True:
            try:
                name = input("Enter your name: ")
                if name == "":
                    raise InvalidInputError("The string cannot be empty!")
                else:
                    return name
            except InvalidInputError as e:
                print(e)


    def choose_level(self):
        while True:
            try:
                round_choice = input("Select game level:\n1 - Short (5 rounds) \n2 - Medium (8 rounds) \n3 - Long (10 rounds) \nYour choice: ")
                if round_choice not in GAME_LEVELS:
                    raise InvalidInputError("Incorrect choice! Try again.")
                else:
                    rounds = GAME_LEVELS[round_choice]
                    return rounds
            except InvalidInputError as e:
                print(e)


    def wait_for_roll(self):
         while True:
            try:
                enter = input("Press Enter")
                if enter != "":
                    raise InvalidRollError("The throw was not made!!! Press ""Enter"" to throw again.")
                else:
                    break
            except InvalidRollError as e:
                print(e)


    def play_round(self, player, computer,round_number):
        player_roll = player.roll_dice()
        computer_roll = computer.roll_dice()
        while player_roll == computer_roll:
            player_roll = player.roll_dice()
            computer_roll = computer.roll_dice()
        if player_roll > computer_roll:
            difference = player_roll - computer_roll
            player.score = player.score + difference
        else:
            difference = computer_roll - player_roll
            player.score = player.score - difference
        result = f"Round {round_number}: \nYou rolled thedice: 🎲 {player_roll} \nThe computer rolled the dice: 🎲 {computer_roll}\nDifference: {difference} points"
        print(result)


    def start_game(self):
        name = self.get_player_name()
        rounds = self.choose_level()
        player = Player(name)
        computer = Computer()
        for i in range(1, rounds + 1):
            self.wait_for_roll()
            self.play_round(player, computer, i)
        print("-"*32)
        print("Game finished!")
        print(f"Date: {self.data}")
        print(f"Name: {name}")
        print(f"Number of rounds: {rounds}")
        print(f"Final score: {player.score}")
        print("-"*32)
        score_manager = ScoreManager()
        score_manager.save_result(name, rounds, player.score)
    


