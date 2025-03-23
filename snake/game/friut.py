"""Fruit"""

import random
import pygame
from pygame import Vector2
from snake.game.config import CELL_SIZE
from snake.game.config import CELL_NUM
from snake.game.colors import Colors


class Fruit:
    """Fruit"""

    def __init__(self):
        self.x = random.randint(0, CELL_NUM - 1)
        self.y = random.randint(0, CELL_NUM - 1)
        self.pos = Vector2(self.x, self.y)

    def randomise(self):
        """randomise"""
        self.x = random.randint(0, CELL_NUM - 1)
        self.y = random.randint(0, CELL_NUM - 1)
        self.pos = Vector2(self.x, self.y)

    def draw(self, window):
        """Draw"""
        fruit_rect = pygame.Rect(
            self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
        )
        pygame.draw.rect(window, Colors.friut, fruit_rect)
