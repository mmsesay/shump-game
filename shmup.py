# Project: Shrump Pygame
# Author: Muhammad Sesay
# Started on: 8TH May 2020
# End on: unknown

# pygame template
import pygame
import random

# constants
WIDTH = 480
HEIGHT = 600
FPS = 60

# default colors
WHITE =  (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE = (0, 0, 255)

# initializations
pygame.init()
pygame.mixer.init()

# create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup")
clock = pygame.time.Clock()

# player sprite class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedX = 0  # this is the player speed

    def update(self):
        self.speedX = 0

        keystate = pygame.key.get_pressed()  # will return a list of all the key pressed
        # check for left key pressed
        if keystate[pygame.K_LEFT]:
            self.speedX = -8

        # check for right key pressed
        if keystate[pygame.K_RIGHT]:
            self.speedX = 8
        
        # move the player
        self.rect.x += self.speedX

        # controll the player from going off the screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# all sprites
all_sprites = pygame.sprite.Group()

# new sprite object
player = Player()
all_sprites.add(player)

# game loop
running = True
while running:
    # this keeps the loop running at the right speed of 30 frames per second
    clock.tick(FPS)

    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False

        # control the player


    # update
    all_sprites.update()

    # draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)  # draw the sprites to the screen

    # *after* drawing everything flip the display
    pygame.display.flip()

# terminate the window
pygame.quit()
