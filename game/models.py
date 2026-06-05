# НЕ ЗАБУДЬ ЗА """"""
from random import randint as rnd

class BasicPlayerSettings:
    def __init__(self):
        self.score = 0

    def roll_dice(self):
        return rnd(1, 6)
    
    def add_score(self):
        self.score = self.score + 1
        return self.score


class Player(BasicPlayerSettings):
    def __init__(self, name):
        self.name = name
        super().__init__()


class Computer(BasicPlayerSettings):
    def __init__(self):
        self.name = "Bot"
        super().__init__()
