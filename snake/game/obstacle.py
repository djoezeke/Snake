"""Obstacles"""

import os
import json
import pathlib
import pygame
from snake.game.config import CELL_NUM, CELL_SIZE
from snake.game.colors import Colors


class Obstacle:
    """Obstacle"""

    _obstacles__: list[list[int]] = []
    _curent_: list[list[int]] = []

    @classmethod
    def load_obstacles(cls, filename: str = ""):
        """load_obstacles"""

        script_dir = pathlib.Path(__file__).parent.parent
        obsatcle_file = os.path.join(
            script_dir,
            os.path.join("assets", filename),
        )
        with open(obsatcle_file, "r", encoding="utf-8") as file:
            cls._obstacles__ = json.load(file)

    @classmethod
    def draw_obstacles(cls, surface: pygame.Surface):
        """draw_obstacles"""
        for row in range(CELL_NUM):
            for col in range(CELL_NUM):
                if cls._obstacles__[row][col] == 1:
                    obstacle_rect = pygame.Rect(
                        col * CELL_SIZE,
                        row * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE,
                    )

                    pygame.draw.rect(surface, Colors.obstacle, obstacle_rect)
