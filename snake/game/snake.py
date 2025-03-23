"""Snake"""

import random
import pygame
from pygame import Vector2
from snake.game.config import CELL_SIZE
from snake.game.config import CELL_NUM
from snake.game.colors import Colors


class Snake:
    """Snake"""

    def __init__(self):
        self.x = random.randint(0, CELL_NUM - 3)
        self.y = random.randint(0, CELL_NUM - 3)
        self.direction = Vector2(1, 0)
        self.body = [
            Vector2(self.x, self.y),
            Vector2(self.x - 1, self.y),
            Vector2(self.x - 2, self.y),
        ]

    def collide_self(self):
        """collide_self"""
        for block in self.body[1:]:
            if block == self.body[0]:
                return True
        return False

    def add_block(self):
        """add_block"""
        body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def draw(self, window):
        """Draw"""
        for block in self.body:
            block_rect = pygame.Rect(
                block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )
            pygame.draw.rect(window, Colors.snake, block_rect)

    def move(self):
        """move"""
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

    def move_left(self):
        """move_left"""
        if self.direction.x != 1:
            self.direction = Vector2(-1, 0)

    def move_right(self):
        """move_right"""
        if self.direction.x != -1:
            self.direction = Vector2(1, 0)

    def move_down(self):
        """move_down"""
        if self.direction.y != -1:
            self.direction = Vector2(0, 1)

    def move_up(self):
        """move_up"""
        if self.direction.y != 1:
            self.direction = Vector2(0, -1)
