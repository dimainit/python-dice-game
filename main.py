# НЕ ЗАБУДЬ ЗА """"""
from game.game import start_game


def main():
    while True:
        print("1. Play")
        print("2. View results")
        print("3. Exit")
        item = input("Select an item: ")
        if item == "1":
            start_game()
        elif item == "2":
            print("Тут будет логика score.py")

        elif item == "3":
            print("Bye!")
            break
        else:
            print("Incorrect choice. Try again.")
main()