# DAMNNNNN!!!!!!!!

import pygame
import sys
import random

pygame.init()

# SCREEN DIMENSIONS
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DAMNNNNN!!!!!")

# BACKGROUND
background = pygame.image.load("background.jpeg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# SOUND
hit_sound = pygame.mixer.Sound("damn-bird-made-with-Voicemod.mp3")

# CHARACTER
character = pygame.image.load("character.png").convert_alpha()
character = pygame.transform.scale(character, (100, 100))

char_rect = character.get_rect()
char_rect.topleft = (random.randint(0, WIDTH -50), random.randint(0, HEIGHT - 50))

# VELOCITY
velocity = [random.choice([-3, 3]), random.choice([-3, 3])]

# CLOCK
clock = pygame.time.Clock()

# MAIN LOOP
running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(character, char_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # MOVE CHARACTER
    char_rect.x += velocity[0]
    char_rect.y += velocity[1]

    # DETECT COLLISION WITH BORDERS
    hit_border = False
    if char_rect.left <= 0 or char_rect.right >= WIDTH:
        velocity[0] *= -1
        hit_border = True
    if char_rect.top <= 0 or char_rect.bottom >= HEIGHT:
        velocity[1] *= -1
        hit_border = True

    # PLAY SOUND ON COLLISION
    if hit_border:
        hit_sound.play()

    # screen.blit(background, (0,0))  # Removed redundant background blit

    pygame.display.flip()

pygame.quit()
sys.exit()