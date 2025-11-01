import pygame
import sys
import random
import math


pygame.init()

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Medieval Angry Birds")

character_one = pygame.image.load (Medieval-Angry-Birds/Images/angrybirdcharactert_transparent_background.png )

enemy_one = pygame.image.load(Medieval-Angry-Birds/Images/second_character.png)

background_image = pygame.image.load(Medieval-Angry-Birds/Images/background.png)
