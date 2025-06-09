"""Fruit"""

import random
import pygame
from pygame import Vector2
from snake.game.config import CELL_SIZE
from snake.game.config import CELL_NUM

# from snake.game.colors import Colors
from snake.game.config import apple


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

    def draw(self, window: pygame.Surface):
        """Draw with pulse effect"""
        import math, time

        scale = 1 + 0.1 * math.sin(time.time() * 5)
        size = int(CELL_SIZE * scale)
        fruit_rect = pygame.Rect(
            self.pos.x * CELL_SIZE + (CELL_SIZE - size) // 2,
            self.pos.y * CELL_SIZE + (CELL_SIZE - size) // 2,
            size,
            size,
        )
        window.blit(pygame.transform.scale(apple, (size, size)), fruit_rect)
