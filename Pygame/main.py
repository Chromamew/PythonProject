import pygame
import sys

def zeichen():
    screen.blit(background, (0,0))
    screen.blit(player, (player_x, player_y))
    pygame.draw.rect(screen, (0,0,0), (100, 100, 5, 100), 0)
    pygame.display.update()

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
# boden 
background = pygame.image.load("Pygame/src/pixilart-drawing.png")
player = pygame.image.load("Pygame/src/player.png")

linkeWand = pygame.draw.rect(screen, (0,0,0), (-2, 0, 5, 700), 0)
rechteWand = pygame.draw.rect(screen, (0,0,0), (701, 0, 5, 700), 0)
neueWand = pygame.draw.rect(screen, (0,0,0), (100,100, 5, 100), 0)
go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    spielerRechteck = pygame.Rect(player_x, player_y, 64,64)
    gedrückt = pygame.key.get_pressed()
    if gedrückt[pygame.K_w]:
        player_y -= geschw
    if gedrückt[pygame.K_d] and not spielerRechteck.colliderect(neueWand):
        player_x += geschw
    if gedrückt[pygame.K_s] and not spielerRechteck.colliderect(linkeWand):
        player_y += geschw
    if gedrückt[pygame.K_a]:
        player_x -= geschw

    
    zeichen()
    

    clock.tick(60)
