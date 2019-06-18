import pygame
import utils
import additionals as ad
import mapGenerator as map
import random
from os import path
mapData = []
mapData = map.load_data(1)
pygame.init()
gameDisplay = pygame.display.set_mode((utils.display_width,utils.display_height))
pygame.display.set_caption("mario iiet")
spritelist = pygame.sprite.Group()
var = 1
coins = 0

#background = pygame.image.load('Game/agh.jpg')


def text_objects(text, fontsize):
    textSurf = fontsize.render(text,True,utils.black)
    return textSurf,textSurf.get_rect()

def coinDrawer(x,y,width,height):
    global coins
    pygame.draw.rect(gameDisplay, utils.red, (x-15, y-15, width+30, height+30))
    pygame.draw.rect(gameDisplay, utils.white, (x-10, y-10, width+20, height+20))
    smallText = pygame.font.Font('bin/coolveticarg.ttf', 25)
    textSurf, textRect = text_objects('Coins: ' +str(coins), smallText)
    textRect.center = (x+(width/2), y+(height/2)-3)
    gameDisplay.blit(textSurf, textRect)

def button(x,y,width,height,inacitive_color,active_color,text):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    flg = False
    pygame.draw.rect(gameDisplay, utils.black, (x-10, y-10, width+20, height+20))
    if mouse[0] > x and mouse[0] < x + width and mouse[1] > y and mouse[1] < y + height:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1:
            flg = True
    else:
        pygame.draw.rect(gameDisplay, inacitive_color, (x,y,width,height))

    smallText = pygame.font.Font('bin/coolveticarg.ttf', 30)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = (x+(width/2), y+(height/2)-3)
    gameDisplay.blit(textSurf, textRect)

    return flg

def game_lost():
    intro = True
    global coins
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(utils.white)
        largeText = pygame.font.Font('bin/coolveticarg.ttf',100)
        text = 'You lost! Coins earned: ' + str(coins)
        textSurf,textRect = text_objects(text,largeText)
        textRect.center = ((utils.display_width/2),(utils.display_height*2/5))
        gameDisplay.blit(textSurf,textRect)
        if button(450, 350, 150, 50, utils.green, utils.lightgreen,'play again'):
            intro = False
            global var
            global mapData
            var = 1
            spritelist.empty()
            mapData = map.load_data(var)
            xD()
            coins = 0
        if button(900, 350, 150, 50, utils.red, utils.lightred, 'exit'):
            pygame.quit()
            quit()
        pygame.display.update()
def game_menu():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(utils.white)

        largeText = pygame.font.Font('bin/coolveticarg.ttf',100)
        textSurf,textRect = text_objects('Mario Iiet edition',largeText)
        textRect.center = ((utils.display_width/2),(utils.display_height*2/5))
        gameDisplay.blit(textSurf,textRect)

        if button(450, 350, 150, 50, utils.green, utils.lightgreen,'start'):
            intro = False
        if button(900, 350, 150, 50, utils.red, utils.lightred, 'exit'):
            pygame.quit()
            quit()

        pygame.display.update()

def xD():
    global spritelist
    for row,tiles in enumerate(mapData):
        for col,tile in enumerate(tiles):
            if tile =='X':
                block = ad.Block(utils.green,col,row)
                block.rect.x = col*utils.tilesize
                block.rect.y = row*utils.tilesize
                spritelist.add(block)
            if tile =='A':
                block = ad.Wall(utils.green,col,row)
                block.rect.x = col*utils.tilesize
                block.rect.y = row*utils.tilesize
                spritelist.add(block)
            if tile =='B':
                block = ad.Wall(utils.green,col,row)
                block.rect.x = col*utils.tilesize
                block.rect.y = row*utils.tilesize
                spritelist.add(block)
            if tile =='P':
                block = ad.Pipe(utils.green,col,row)
                block.rect.x = col*utils.tilesize
                block.rect.y = row*utils.tilesize
                spritelist.add(block)
            if tile =='D':
                block = ad.Destroyable(utils.green,col,row)
                block.rect.x = col*utils.tilesize
                block.rect.y = row*utils.tilesize
                spritelist.add(block)
            if tile =='C':
                block = ad.Coins(utils.green,col,row)
                block.rect.x = col*utils.tilesize
                block.rect.y = row*utils.tilesize
                spritelist.add(block)
            if tile =='S':
                block = ad.Spikes(utils.green,col,row)
                block.rect.x = col*utils.tilesize
                block.rect.y = row*utils.tilesize
                spritelist.add(block)
            if tile =='H':
                block = ad.HiddenOff(utils.black,col,row)
                block.rect.x = col*utils.tilesize
                block.rect.y = row*utils.tilesize
                spritelist.add(block)

def game_loop():
    global mapData
    flag = True
    x = 32
    y = 480
    char_width = 20
    char_height = 32
    vel = 10
    gravity = 10
    jumps = 0
    jumpedBefore = 0 #flaga określająca czy w poprzedniej klatce został wykonany skok
    left = False
    right = False
    walkcount = 0
    framerate = 25
    walkright = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png')]
    walkleft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png')]
    character = pygame.image.load('Game/Standing.png')
    clock = pygame.time.Clock()
    xD()
    character1 = ad.Character(utils.red,char_width,char_height)
    character1.rect.x = x
    character1.rect.y = y

    def check_down_collision():
        nonlocal y
        nonlocal x
        nonlocal jumps
        global coins
        if y > utils.display_height - char_height:
            y = utils.display_height - char_height
            jumps = 0
        for sprite in spritelist:
            if isinstance(sprite, ad.HiddenOff):
                pass
            elif pygame.sprite.collide_rect(sprite, character1):
                if isinstance(sprite, ad.Coins):
                    coins += 1
                    sprite.kill()
                else:
                    y = sprite.rect.y - char_height
                    character1.rect.y = y
                    jumps = 0
                if isinstance(sprite,ad.Spikes):
                    x = 32
                    y = 480
                    character1.rect.x = x
                    character1.rect.y = y
                    game_lost()


    def check_up_collision():
        nonlocal y
        global spritelist
        nonlocal jumpcount
        global coins
        for sprite in spritelist:
            if pygame.sprite.collide_rect(sprite, character1):
                if isinstance(sprite, ad.Coins):
                    coins += 1
                    sprite.kill()
                else:
                    y = sprite.rect.y + sprite.rect.height
                    character1.rect.y = y
                    jumpcount = 0
                if isinstance(sprite, ad.Destroyable):
                    sprite.kill()
                elif isinstance(sprite, ad.HiddenOff):
                    block = ad.HiddenOn(utils.green, x//utils.tilesize, y//utils.tilesize)
                    block.rect.x = sprite.rect.x
                    block.rect.y = sprite.rect.y
                    sprite.kill()
                    spritelist.add(block)

    def check_right_collision():
        nonlocal x
        global coins
        for sprite in spritelist:
            if isinstance(sprite, ad.HiddenOff):
                pass
            elif pygame.sprite.collide_rect(sprite, character1):
                if isinstance(sprite, ad.Coins):
                    coins += 1
                    sprite.kill()
                else:
                    x = sprite.rect.x - char_width
                    character1.rect.x = x
    def check_left_collision():
        nonlocal x
        global coins
        for sprite in spritelist:
            if isinstance(sprite, ad.HiddenOff):
                pass
            elif pygame.sprite.collide_rect(sprite, character1):
                if isinstance(sprite, ad.Coins):
                    coins += 1
                    sprite.kill()
                else:
                    x = sprite.rect.x + sprite.rect.width
                    character1.rect.x = x

    def redraw():
        global spritelist
        nonlocal walkcount
        global gameDisplay
        gameDisplay.fill(utils.black)
        spritelist.draw(gameDisplay)
        if walkcount + 1 >= 12:
            walkcount = 0

        if left:
            gameDisplay.blit(walkleft[walkcount//3], (x,y))
            walkcount += 1
        elif right:
            gameDisplay.blit(walkright[walkcount // 3], (x,y))
            walkcount += 1
        else:
            gameDisplay.blit(character, (x,y))
        coinDrawer(50,50,80,10)
        pygame.display.update()


    while flag:
        clock.tick(framerate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        y += gravity
        character1.rect.y = y
        check_down_collision()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and x > vel:
            x -= vel
            character1.rect.x = x
            check_left_collision()
            right = False
            left = True
        elif key[pygame.K_RIGHT]:
            x += vel
            character1.rect.x = x
            check_right_collision()
            right = True
            left = False
        else:
            right = False
            left = False

        if key[pygame.K_UP] and jumps < 2 and jumpedBefore == 0:
            jumps += 1
            jumpcount = 7
            jumpedBefore = 4
        elif jumpedBefore > 0:
            jumpedBefore -= 1
        if jumps > 0 and jumpcount >= 0:
            y -= min(abs(jumpcount) * jumpcount,30)
            character1.rect.y = y
            check_up_collision()
            jumpcount -= 1
        if x >= utils.display_width:
            global var
            global mapData
            var = var + 1
            spritelist.empty()
            mapData = map.load_data(var)
            xD()
            x = 0
            character1.rect.x = 0
        redraw()

game_menu()
game_loop()
