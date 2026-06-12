from game.game import DiceGame
from game.score import ScoreManager

def main():
    while True:
        print("1. Play")
        print("2. View results")
        print("3. Exit")
        item = input("Select an item: ")
        if item == "1":
            game = DiceGame()
            game.start_game()
        elif item == "2":
            score_manager = ScoreManager()
            score_manager.get_results()
        elif item == "3":
            print("Bye!")
            break
        else:
            print("Incorrect choice. Try again.")
main()