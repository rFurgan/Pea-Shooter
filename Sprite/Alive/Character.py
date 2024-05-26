import pygame
from Sprite.Sprite import Sprite
from Sprite.Alive.Bullet import Bullet
from Common.Constants import DIRECTION

class Character(Sprite):
    def __init__(self, x, y, width, height, color, speed_x, speed_y):
        super().__init__(x, y, height, width, color)
        self.SPEED_X = speed_x
        self.SPEED_Y = speed_y
        self.is_jumping = False
        self.jump_height = 120
        self.max_jump_height = 0
        self.direction = DIRECTION.RIGHT

    def move_lr(self, direction, delta_time):
        self.direction = direction
        self.rect.x += self.SPEED_X * direction.value * delta_time

    def move_ud(self, direction, delta_time):
        # self.direction = direction
        self.rect.y += self.SPEED_Y * direction.value * delta_time
    
    def shoot(self):
        bullet_dimension = 5
        bullet_offset = 1
        x = self.rect.x + self.rect.width + bullet_offset if self.direction == DIRECTION.RIGHT else self.rect.x - bullet_dimension - bullet_offset
        return Bullet(x, self.rect.y + 20, bullet_dimension, bullet_dimension, (255, 255, 255), .6, self.direction)

    def jump(self):
        if (not self.is_jumping):
            self.is_jumping = True
            self.max_jump_height = self.rect.y - self.jump_height

    def jumping(self, delta_time):
        if (self.is_jumping):
            if (self.rect.y > self.max_jump_height):
                self.move_ud(DIRECTION.UP, delta_time)
            else:
                self.is_jumping = False

    def gravity(self, tiles, delta_time):
        if (len(pygame.sprite.spritecollide(self, tiles, False)) == 0):
            if (not self.is_jumping):
                self.move_ud(DIRECTION.DOWN, delta_time)
