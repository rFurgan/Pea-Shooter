from Sprite.Sprite import Sprite

class Bullet(Sprite):
    def __init__(self, x, y, width, height, color, speed_x, direction):
        super().__init__(x, y, height, width, color)
        self.SPEED_X = speed_x
        self.DAMAGE = 100
        self.DIRECTION = direction

    def move(self, delta_time):
        self.rect.x += (round(self.SPEED_X) * self.DIRECTION.value * delta_time)
