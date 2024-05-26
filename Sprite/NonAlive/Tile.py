from Sprite.Sprite import Sprite

class Tile(Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, height, width, color)
