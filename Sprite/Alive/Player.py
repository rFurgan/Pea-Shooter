from Sprite.Alive.Character import Character

class Player(Character):
    def __init__(self, x, y, width, height, color):
        self.SPEED_X = 0.2
        self.SPEED_Y = 0.4
        super().__init__(x, y, height, width, color, self.SPEED_X, self.SPEED_Y)
