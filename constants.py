from math import sqrt
import pygame

LENGTH, HEIGHT = 800, 600 # Fills the screen on an Amazon Fire 7

DIAGONAL_DISTANCE = sqrt(2)
DIAGONAL_DISTANCE_REPR = "√2"
NODE_LENGTH_DISTANCE, NODE_WIDTH_DISTANCE, STAIR_DISTANCE = 40, 33, 43

WHITE = (255, 255, 255) # 100% Luminosity
BLACK = (0, 0, 0) # 0%
GREY = (128, 128, 128) # 50%

BLUE = (0, 0, 240) # Most classrooms
BROWN = (160, 82, 45) # Some classrooms
LIGHT_BROWN = (255, 248, 220) # Some classrooms

GREEN = (0, 230, 0)
RED = (230, 0, 0)
YELLOW = (255, 255, 0)

pygame.font.init()
MICRO_FONT = pygame.font.SysFont("comicsans", 7)
TINY_FONT = pygame.font.SysFont("comicsans", 8)
MINI_FONT = pygame.font.SysFont("comicsans", 9)
MEDIUM_FONT = pygame.font.SysFont("comicsans", 10)
BIG_FONT = pygame.font.SysFont("comicsans", 25)
HUGE_FONT = pygame.font.SysFont("comicsans", 40)

def decimal_range(start, stop, step=1):
    value = start

    while value < stop:
        yield value
        value += step
