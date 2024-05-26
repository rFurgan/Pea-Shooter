import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, left, top, height, width, color):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))   
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top