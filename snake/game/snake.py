"""Snake"""

import random
import pygame
from pygame import Vector2
from snake.game.config import CELL_SIZE
from snake.game.config import CELL_NUM

# from snake.game.colors import Colors
from snake.game.config import (
    body_bl,
    body_br,
    body_horizontal,
    body_tl,
    body_tr,
    body_vertical,
    tail_down,
    tail_left,
    tail_right,
    tail_up,
    head_down,
    head_left,
    head_right,
    head_up,
)


class Snake:
    """Snake"""

    def __init__(self):
        self.x = random.randint(0, CELL_NUM - 3)
        self.y = random.randint(0, CELL_NUM - 3)
        self.direction = Vector2(1, 0)
        self.new_block = False
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
        # for block in self.body:
        #     block_rect = pygame.Rect(
        #         block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
        #     )
        #     pygame.draw.rect(window, Colors.snake, block_rect)
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)

            if index == 0:
                window.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                window.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    window.blit(body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    window.blit(body_horizontal, block_rect)
                else:
                    if (
                        previous_block.x == -1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == -1
                    ):
                        window.blit(body_tl, block_rect)
                    elif (
                        previous_block.x == -1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == -1
                    ):
                        window.blit(body_bl, block_rect)
                    elif (
                        previous_block.x == 1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == 1
                    ):
                        window.blit(body_tr, block_rect)
                    elif (
                        previous_block.x == 1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == 1
                    ):
                        window.blit(body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = head_left
        elif head_relation == Vector2(-1, 0):
            self.head = head_right
        elif head_relation == Vector2(0, 1):
            self.head = head_up
        elif head_relation == Vector2(0, -1):
            self.head = head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = tail_down

    def move(self):
        """move"""
        if self.new_block == True:
            self.add_block()
        else:
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
