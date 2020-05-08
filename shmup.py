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
YELLOW = (255, 255, 0)

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

    # shoot function
    def shoot(self):
        # creating an instance of the bullet
        self.bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(self.bullet)
        bullets.add(self.bullet)

# mob sprite class
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # check the mob state matches any of the conditions, respawn them
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


# bullet sprite
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill remove the sprite from the group
        if self.rect.bottom < 0:
            self.kill() 


# all sprites groups
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# new player sprite object
player = Player()
all_sprites.add(player)

# new mob sprite object
for i in range(8):
    mob = Mob()
    all_sprites.add(mob)
    mobs.add(mob)

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

        # control the player shoot event
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()  # call the player shoot function


    # update
    all_sprites.update()

    # check if a mob collide with a bullet and destroy both (mob and bullet)
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    # respawn mob when killed
    for hit in hits:
        mob = Mob()  # create new Mob instance
        all_sprites.add(mob)  # add the mob sprite
        mobs.add(mob)  # add it to the group


    # check for player and mob collision
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

    # draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)  # draw the sprites to the screen

    # *after* drawing everything flip the display
    pygame.display.flip()

# terminate the window
pygame.quit()
