import pygame
import sys

#basic parameters
pygame.init()
clock = pygame.time.Clock()
screen_x = 600
screen_y = 600
screen = pygame.display.set_mode([screen_x, screen_y])

# boden 
boden = pygame.Rect(0, screen_y - 50, screen_x, 50)
player = pygame.Rect(30, screen_y-90, 20,20)

go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if 





    screen.fill((25,25,25))
    #wo, farbe            posx,posy,breite,höhe
    (screen,(50,150,200),(0, screen_y-50, screen_x, 50))

    pygame.draw.rect(screen, (50,100,200), boden)
    pygame.draw.rect(screen, (200, 0, 100), player)
    pygame.display.update()


    clock.tick(60)
