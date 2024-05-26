import sys
import pygame
from Sprite.Alive.Player import Player
from Common.Constants import FPS, WINDOW_SIZE, DIRECTION
from Level.Level import load_level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Pea Shooter") 
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.all_sprites = pygame.sprite.Group()
        self.character_sprites = pygame.sprite.Group()
        self.tile_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.delta_time = 0

        self.player = Player(200, 110, 50, 50, (255, 0, 255))
        tiles, enemies = load_level("01")
        self.all_sprites.add([self.player, tiles, enemies])
        self.character_sprites.add([self.player, enemies])
        self.tile_sprites.add([tiles])

    def keyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                elif event.key == pygame.K_LCTRL:
                    bullet = self.player.shoot()
                    self.all_sprites.add(bullet)
                    self.bullet_sprites.add(bullet)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.player.move_lr(DIRECTION.LEFT, self.delta_time)
        elif key[pygame.K_RIGHT]:
            self.player.move_lr(DIRECTION.RIGHT, self.delta_time)

    def is_gone(self):
        for sprite in self.all_sprites:
            if (sprite.rect.y > self.window.get_height() - 100):
                self.all_sprites.remove(sprite)
            elif (sprite.rect.x < 0 or sprite.rect.x + sprite.rect.width > self.window.get_width()):
                self.all_sprites.remove(sprite)

    def gravity_and_jump(self):
        for character_sprite in self.character_sprites:
            character_sprite.gravity(self.tile_sprites, self.delta_time)
            character_sprite.jumping(self.delta_time)

    def bullet(self):
        for bullet_sprite in self.bullet_sprites:
            bullet_sprite.move(self.delta_time)
            if (pygame.sprite.spritecollide(bullet_sprite, self.character_sprites, True) == 0):
                self.all_sprites.remove(bullet_sprite)
                self.bullet_sprites.remove(bullet_sprite)

    def start(self):
        while not self.game_over:
            self.delta_time = self.clock.tick(FPS)
            self.keyboard()
            self.all_sprites.update()
            self.window.fill((0,0,0))
            self.all_sprites.draw(self.window)
            self.gravity_and_jump()
            self.bullet()
            self.is_gone()
            pygame.display.flip()
