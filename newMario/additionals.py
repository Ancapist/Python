import pygame
import utils

class Block(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.image.load("Game/block.png")
        self.rect = self.image.get_rect()
        self.rect.x = x * utils.tilesize
        self.rect.y = y * utils.tilesize

class Wall(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.image.load("Game/wall.png")
        self.rect = self.image.get_rect()
        self.rect.x = x * utils.tilesize
        self.rect.y = y * utils.tilesize

class Character(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(utils.white)
        self.image.set_colorkey(utils.white)
        pygame.draw.rect(self.image, utils.white, [0, 0, width, height])
        self.rect = self.image.get_rect()

class Pipe(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.image.load("Game/pipe.png")
        self.rect = self.image.get_rect()
        self.rect.x = x * utils.tilesize
        self.rect.y = y * utils.tilesize

class Destroyable(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.image.load("Game/destroyable.png")
        self.rect = self.image.get_rect()
        self.rect.x = x * utils.tilesize
        self.rect.y = y * utils.tilesize

class Coins(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.image.load("Game/coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = x * utils.tilesize
        self.rect.y = y * utils.tilesize

class Spikes(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.image.load("Game/spikes.png")
        self.rect = self.image.get_rect()
        self.rect.x = x * utils.tilesize
        self.rect.y = y * utils.tilesize

class HiddenOff(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        self.image = pygame.Surface([utils.tilesize, utils.tilesize])
        self.image.fill(utils.white)
        self.image.set_colorkey(utils.white)
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.x = x * utils.tilesize
        self.rect.y = y * utils.tilesize

class HiddenOn(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.image.load("Game/pipe.png")
        self.rect = self.image.get_rect()
        self.rect.x = x * utils.tilesize
        self.rect.y = y * utils.tilesize