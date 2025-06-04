"""Game Options"""

import os
import pygame


def get_resource(filename):
    "Get Assets"
    asset = os.path.join("snake", "assets", filename)
    return asset


def get_sound(filename: str):
    "Get Sound"
    sound = os.path.join(get_resource("sounds"), filename)
    return sound


def get_image(filename: str):
    "Get Image"
    icon = os.path.join(get_resource("images"), filename)
    return icon


def get_font(filename: str):
    "Get Font"
    font = os.path.join(get_resource("fonts"), filename)
    return font


def flip_button_image(img, flip_horizontal, flip_vertical):
    """Flip images"""
    img_copy = img.copy()
    img_flip = pygame.transform.flip(img_copy, flip_horizontal, flip_vertical)
    return img_flip


VERSION: str = "1.0.0"
DEBUG: bool = True

CELL_SIZE = 30
CELL_NUM = 20
HEIGHT: int = CELL_NUM * CELL_SIZE  # Game Window height
WIDTH: int = CELL_NUM * CELL_SIZE  # Game Window Width
SCREEN: dict = (WIDTH, HEIGHT)  # Game Screen

FPS: int = 60

WINDOW: pygame.Surface = pygame.display.set_mode(SCREEN)

# clock info
clock: pygame.Clock = pygame.time.Clock()

# Images

apple: pygame.Surface = pygame.image.load(get_image("apple.png"))
apple = pygame.transform.scale(apple, (CELL_SIZE, CELL_SIZE))

body_bl: pygame.Surface = pygame.image.load(get_image("body_bl.png"))
body_bl = pygame.transform.scale(body_bl, (CELL_SIZE, CELL_SIZE))

body_br: pygame.Surface = pygame.image.load(get_image("body_br.png"))
body_br = pygame.transform.scale(body_br, (CELL_SIZE, CELL_SIZE))

body_tl: pygame.Surface = pygame.image.load(get_image("body_tl.png"))
body_tl = pygame.transform.scale(body_tl, (CELL_SIZE, CELL_SIZE))

body_tr: pygame.Surface = pygame.image.load(get_image("body_tr.png"))
body_tr = pygame.transform.scale(body_tr, (CELL_SIZE, CELL_SIZE))

head_up: pygame.Surface = pygame.image.load(get_image("head_up.png"))
head_up = pygame.transform.scale(head_up, (CELL_SIZE, CELL_SIZE))

head_left: pygame.Surface = pygame.image.load(get_image("head_left.png"))
head_left = pygame.transform.scale(head_left, (CELL_SIZE, CELL_SIZE))

head_right: pygame.Surface = pygame.image.load(get_image("head_right.png"))
head_right = pygame.transform.scale(head_right, (CELL_SIZE, CELL_SIZE))

head_down: pygame.Surface = pygame.image.load(get_image("head_down.png"))
head_down = pygame.transform.scale(head_down, (CELL_SIZE, CELL_SIZE))

tail_up: pygame.Surface = pygame.image.load(get_image("tail_up.png"))
tail_up = pygame.transform.scale(tail_up, (CELL_SIZE, CELL_SIZE))

tail_left: pygame.Surface = pygame.image.load(get_image("tail_left.png"))
tail_left = pygame.transform.scale(tail_left, (CELL_SIZE, CELL_SIZE))

tail_right: pygame.Surface = pygame.image.load(get_image("tail_right.png"))
tail_right = pygame.transform.scale(tail_right, (CELL_SIZE, CELL_SIZE))

tail_down: pygame.Surface = pygame.image.load(get_image("tail_down.png"))
tail_down = pygame.transform.scale(tail_down, (CELL_SIZE, CELL_SIZE))

body_horizontal: pygame.Surface = pygame.image.load(get_image("body_horizontal.png"))
body_horizontal = pygame.transform.scale(body_horizontal, (CELL_SIZE, CELL_SIZE))

body_vertical: pygame.Surface = pygame.image.load(get_image("body_vertical.png"))
body_vertical = pygame.transform.scale(body_vertical, (CELL_SIZE, CELL_SIZE))

# Fonts
pygame.font.init()  # initialize pygame font

font: pygame.Font = pygame.font.Font(None, 40)

# Sounds
pygame.mixer.init()  # initialize pygame mixer
volume: float = 0.3  # music volume

music: pygame.Sound = pygame.mixer.Sound(get_sound("music.wav"))
crunch: pygame.Sound = pygame.mixer.Sound(get_sound("crunch.wav"))
music_c = pygame.Channel(1)
music_c.set_volume(0.3)
crunch_c = pygame.Channel(2)
crunch_c.set_volume(1)
# Icons

# Rects
