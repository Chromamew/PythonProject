import pygame
import random
import math


class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.background_img = pygame.image.load("spr_space_himmel.png")
        pygame.display.set_caption("Space Invaders")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.speed = 10
        self.spaceship = Spaceship(self, 370, 515)
        self.enemys = []
        self.item = Items(self, 100, 100)
        self.score = 0
        for i in range(12):
            self.enemys.append(Enemy(self, random.randint(0, 736), random.randint(30, 130)))


        while self.running:

            self.clock.tick(60)
            self.screen.blit(self.background_img, (0, 0))
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.spaceship.move(-self.speed)

                    if event.key == pygame.K_d:
                        self.spaceship.move(self.speed)
                    if event.key == pygame.K_SPACE:
                        self.spaceship.fire_bullet()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.spaceship.move(self.speed)
                    if event.key == pygame.K_d:
                        self.spaceship.move(-self.speed)

                if event.type == pygame.QUIT:
                    self.running = False

            self.spaceship.update()

            if len(self.spaceship.bullets) > 0:
                for bullet in self.spaceship.bullets:
                    if bullet.is_fired:
                        bullet.update()
                    else:
                        self.spaceship.bullets.remove(bullet)

            for enemy in self.enemys:
                enemy.update()
                enemy.check_collision()
                if enemy.pos_y > 500:
                    for i in self.enemys:
                        i.pos_y = 1000
                    self.print_game_over()
                    break
            self.print_score()
            pygame.display.update()
    def print_game_over(self):
        go_font = pygame.font.Font("freesansbold.ttf", 64)
        go_text = go_font.render("Game Over", True, (255, 255, 255))
        self.screen.blit(go_text, (200, 250))

    def print_score(self):
        score_font = pygame.font.Font("freesansbold.ttf", 32)
        score_text = score_font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (8, 8))

class Spaceship:
    def __init__(self, game, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.change_x = 0
        self.game = game
        self.spaceship_img = pygame.image.load("spr_spaceship.png")
        self.bullets = []

    def move(self, speed):
        self.change_x += speed

    def update(self):
        self.x_pos += self.change_x
        if self.x_pos < 0:
            self.x_pos = 0
        elif self.x_pos > 736:
            self.x_pos = 736
        self.game.screen.blit(self.spaceship_img, (self.x_pos, self.y_pos))

    def fire_bullet(self):
        self.bullets.append(Bullet(self.game, self.x_pos, self.y_pos))
        self.bullets[len(self.bullets) - 1].fire()


class Bullet:
    def __init__(self, game, pos_x, pos_y):
        self.game = game
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.bullet_img = pygame.image.load("spr_patrone.png")
        self.is_fired = False
        self.bullet_speed = 10

    def fire(self):
        self.is_fired = True

    def update(self):
        self.pos_y -= self.bullet_speed
        if self.pos_y <= 0:
            self.is_fired = False
        self.game.screen.blit(self.bullet_img, (self.pos_x, self.pos_y))


class Enemy:
    def __init__(self, game, pos_x, pos_y):
        self.game = game
        self. pos_x = pos_x
        self.pos_y = pos_y
        self.enemy_img = pygame.image.load("spr_space_enemy.png")
        self.change_x = 5
        self.change_Y = 60

    def check_collision(self):
        for bullet in self.game.spaceship.bullets:
            distance = math.sqrt(math.pow(self.pos_x-bullet.pos_x, 2) + math.pow(self.pos_y - bullet.pos_y, 2))
            if distance < 35:
                bullet.is_fired = False
                self.pos_x = random.randint(0, 736)
                self.pos_y = random.randint(0, 150)
                self.game.score += 1
                self.game.item.update()



    def update(self):
        self.pos_x += self.change_x
        if self.pos_x >= 736:
            self.pos_y += self.change_Y
            self.change_x = -5
        elif self.pos_x <= 0:
            self.pos_y += self.change_Y
            self.change_x += 5
        self.game.screen.blit(self.enemy_img, (self.pos_x, self.pos_y))



class Items:
    def __init__(self, game, pos_x, pos_y):
        self.game = game
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.fall_speed = 5
        self.collectable = False
        self.powerup_img = pygame.image.load("spr_powerup.png")

    def update(self):
        self.pos_y += self.fall_speed
        if self.pos_y <= 0:
            self.collectable = False
        self.game.screen.blit(self.powerup_img, (self.game.enemys[0].pos_x, self.game.enemys[0].pos_y))

    def spwned(self):
        self.collectable = True



if __name__ == "__main__":
    game = Game(800, 600)