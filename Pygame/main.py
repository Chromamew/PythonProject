import pygame
import sys

#basic parameters
pygame.init()
clock = pygame.time.Clock()
screen_x = 600
screen_y = 600
player_x = 100
player_y = 440
screen = pygame.display.set_mode([screen_x, screen_y])

# boden 
boden = pygame.image.load("Pygame/src/gras_floor.png")
background = pygame.image.load("Pygame/src/background.png")
player = pygame.image.load("Pygame/src/horst.png")


go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((25,25,25))
    #wo, farbe            posx,posy,breite,höhe
    (screen,(50,150,200),(0, screen_y-50, screen_x, 50))

    screen.blit(background, (0,0))
    screen.blit(boden, (0, 550))
    screen.blit(player, (player_x, player_y))
    pygame.display.update()


    clock.tick(60)
