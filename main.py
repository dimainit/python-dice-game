from game.game import start_game
from game.score import get_results

def main():
    while True:
        print("1. Play")
        print("2. View results")
        print("3. Exit")
        item = input("Select an item: ")
        if item == "1":
            start_game()
        elif item == "2":
            get_results()
        elif item == "3":
            print("Bye!")
            break
        else:
            print("Incorrect choice. Try again.")
main()