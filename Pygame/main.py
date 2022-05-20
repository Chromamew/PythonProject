from operator import ge
import pygame
import sys

#basic parameters
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame")
screen_x = 700
screen_y = 700
player_x = 100
player_y = 600
geschw = 8

screen = pygame.display.set_mode([screen_x, screen_y])

rechteWand = pygame.draw.rect(screen, (0,0,0), (screen_x-2, 0, 2, 700), 0)
linkeWand = pygame.draw.rect(screen, (0,0,0), (screen_y+1, 0, 2, 700), 0)




# boden 
background = pygame.image.load("Pygame/src/pixilart-drawing.png")
player = pygame.image.load("Pygame/src/player.png")


go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    spielerRechteck = pygame.Rect(player_x, player_y, 64,64)
    gedrückt = pygame.key.get_pressed()
    if gedrückt[pygame.K_w]:
        player_y -= geschw
    if gedrückt[pygame.K_d] and not spielerRechteck.colliderect(rechteWand):
        player_x += geschw
    if gedrückt[pygame.K_s] and not spielerRechteck.colliderect(linkeWand):
        player_y += geschw
    if gedrückt[pygame.K_a]:
        player_x -= geschw

    screen.fill((25,25,25))
    #wo, farbe            posx,posy,breite,höhe
    #(screen,(50,150,200),(0, screen_y-50, screen_x, 50))

    screen.blit(background, (0,0))
    screen.blit(player, (player_x, player_y))
    pygame.display.update()


    clock.tick(60)
