"""Settings for controls and graphics"""

import pygame

DEFAULT_CONTROLS = {
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
}


class Settings:
    def __init__(self):
        self.controls = DEFAULT_CONTROLS.copy()
        self.show_grass = True

    def set_control(self, action, key):
        self.controls[action] = key

    def toggle_grass(self):
        self.show_grass = not self.show_grass


settings = Settings()
