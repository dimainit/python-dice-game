from random import randint as rnd

class BasicPlayerSettings:
    """
    Base class for shared player logic.
    Stores score and contains dice roll method.
    Player and Computer inherit this logic.
    """
    def __init__(self):
        self.score = 0

    def roll_dice(self):
        return rnd(1, 6)
    
    def add_score(self):
        self.score = self.score + 1
        return self.score


class Player(BasicPlayerSettings):
    """
    Represents a real user.
    Stores the player's name and score, inherited from     BasicPlayerSettings using the super() function.
    """
    def __init__(self, name):
        self.name = name
        super().__init__()


class Computer(BasicPlayerSettings):
    """ Represents the computer opponent. Uses default name and score inherited from Basic PlayerSettings. """
    def __init__(self):
        self.name = "Bot"
        super().__init__()
