"""MAin Game"""

import sys
import pygame

from snake.game import config
from snake.game.colors import Colors
from snake.game.friut import Fruit
from snake.game.snake import Snake
from snake.game.obstacle import Obstacle
from snake.game.settings import settings

SNAKE_MOVE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_MOVE, 200)

UPDATE_SCORE = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATE_SCORE, 1500)


class Game:
    """Game"""

    def __init__(self):
        self.fruit = Fruit()
        self.snake = Snake()
        self.score = 0
        self.highscore = 0
        self.paused = False
        self.game_over = False
        Obstacle.load_obstacles("obstacle.json")

    def update_score(self):
        """update_score"""
        if self.game_over is False and self.paused is False:
            self.score += 1
            if self.score > self.highscore:
                self.highscore = self.score

    def update(self):
        """update"""
        if self.game_over is False and self.paused is False:
            self.snake.move()

    def snake_out(self):
        """snake_out"""
        if not 0 <= self.snake.body[0].x < config.CELL_NUM:
            self.game_over = True
        if not 0 <= self.snake.body[0].y < config.CELL_NUM:
            self.game_over = True

    def draw_grass(self, window):
        """draw_grass"""
        if not settings.show_grass:
            return
        for row in range(config.CELL_NUM):
            if row % 2 == 0:
                for col in range(config.CELL_NUM):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * config.CELL_SIZE,
                            row * config.CELL_SIZE,
                            config.CELL_SIZE,
                            config.CELL_SIZE,
                        )
                        pygame.draw.rect(window, Colors.grass, grass_rect)
        Obstacle.draw_obstacles(window)

    def collision(self):
        """collision"""

        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomise()
            self.snake.add_block()
            config.crunch_c.play(config.crunch)
            # self.score += 5

        if self.snake.collide_self():
            self.game_over = True

        self.snake_out()

    def reset(self):
        """reset"""

        self.fruit = Fruit()
        self.snake = Snake()
        self.score = 0
        self.paused = False
        self.game_over = False

    def draw(self, screen: pygame.Surface):
        """draw"""
        score_suface = config.font.render("Score", True, Colors.white)
        highscore_surface = config.font.render(
            f"High Score: {self.highscore}", True, Colors.white
        )
        over_suface = config.font.render("GAME OVER", True, Colors.white)
        paused_suface = config.font.render("GAME PAUSED", True, Colors.white)

        score_value_suface = config.font.render(f"{self.score}", True, Colors.white)

        screen.fill(Colors.background)
        self.draw_grass(screen)

        self.fruit.draw(screen)
        self.snake.draw(screen)
        self.collision()

        screen.blit(score_suface, (10, 20, 50, 50))
        screen.blit(score_value_suface, (100, 20, 50, 50))
        screen.blit(highscore_surface, (10, 60, 200, 50))

        if self.paused:
            screen.blit(
                paused_suface, ((config.WIDTH / 2) - 100, config.HEIGHT / 2, 50, 50)
            )

        if self.game_over:
            screen.blit(
                over_suface, ((config.WIDTH / 2) - 100, config.HEIGHT / 2, 50, 50)
            )

    def show_menu(self, screen):
        """Display start menu"""
        screen.fill(Colors.background)
        title = config.font.render("SNAKE GAME", True, Colors.white)
        start = config.font.render("Press ENTER to Start", True, Colors.white)
        screen.blit(title, ((config.WIDTH // 2) - 100, config.HEIGHT // 2 - 60))
        screen.blit(start, ((config.WIDTH // 2) - 140, config.HEIGHT // 2))
        pygame.display.update()

    def show_game_over(self, screen):
        """Display game over screen"""
        screen.fill(Colors.background)
        over = config.font.render("GAME OVER", True, Colors.white)
        restart = config.font.render("Press ENTER to Restart", True, Colors.white)
        score = config.font.render(f"Score: {self.score}", True, Colors.white)
        screen.blit(over, ((config.WIDTH // 2) - 100, config.HEIGHT // 2 - 60))
        screen.blit(score, ((config.WIDTH // 2) - 60, config.HEIGHT // 2))
        screen.blit(restart, ((config.WIDTH // 2) - 160, config.HEIGHT // 2 + 60))
        pygame.display.update()

    def move_left(self):
        """move_left"""
        if self.game_over is False and self.paused is False:
            self.snake.move_left()

    def move_right(self):
        """move_right"""
        if self.game_over is False and self.paused is False:
            self.snake.move_right()

    def move_down(self):
        """move_down"""

        if self.game_over is False and self.paused is False:
            self.snake.move_down()

    def move_up(self):
        """move_up"""
        if self.game_over is False and self.paused is False:
            self.snake.move_up()

    def show_settings_menu(self, screen):
        """Display settings menu for controls and graphics"""
        waiting = True
        selected = 0
        options = ["Left", "Right", "Up", "Down", "Toggle Grass", "Back"]
        actions = ["left", "right", "up", "down"]

        while waiting:
            screen.fill(Colors.background)
            title = config.font.render("SETTINGS", True, Colors.white)
            screen.blit(title, ((config.WIDTH // 2) - 80, 60))
            for i, opt in enumerate(options):
                color = Colors.friut if i == selected else Colors.white
                if opt in ["Left", "Right", "Up", "Down"]:
                    key_name = pygame.key.name(settings.controls[actions[i]])
                    text = config.font.render(f"{opt}: {key_name.upper()}", True, color)
                elif opt == "Toggle Grass":
                    state = "ON" if settings.show_grass else "OFF"
                    text = config.font.render(f"{opt}: {state}", True, color)
                else:
                    text = config.font.render(opt, True, color)
                screen.blit(text, (100, 140 + i * 50))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        if selected < 4:
                            # Remap control
                            remap = True
                            while remap:
                                info = config.font.render(
                                    "Press new key...", True, Colors.friut
                                )
                                screen.blit(info, (100, 440))
                                pygame.display.update()
                                for e in pygame.event.get():
                                    if e.type == pygame.KEYDOWN:
                                        settings.set_control(actions[selected], e.key)
                                        remap = False
                        elif options[selected] == "Toggle Grass":
                            settings.toggle_grass()
                        elif options[selected] == "Back":
                            waiting = False

    def show_pause_menu(self, screen):
        """Display pause overlay with options"""
        paused = True
        selected = 0
        options = ["Resume", "Settings", "Quit"]
        while paused:
            screen.fill(Colors.background)
            overlay = pygame.Surface((config.WIDTH, config.HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))
            title = config.font.render("PAUSED", True, Colors.white)
            screen.blit(title, ((config.WIDTH // 2) - 80, 100))
            for i, opt in enumerate(options):
                color = Colors.friut if i == selected else Colors.white
                text = config.font.render(opt, True, color)
                screen.blit(text, (config.WIDTH // 2 - 60, 200 + i * 60))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        if options[selected] == "Resume":
                            paused = False
                        elif options[selected] == "Settings":
                            show_settings_menu(screen)
                        elif options[selected] == "Quit":
                            pygame.quit()
                            exit()


game = Game()


def snake(args: list):
    """snake"""

    pygame.display.set_caption("Snake")
    config.music_c.play(config.music, loops=-1)

    if "--nosound" in args:
        config.music_c.set_volume(0)
        config.music_c.stop()
        config.crunch_c.set_volume(0)
        config.crunch_c.stop()

    menu = True
    while menu:
        game.show_menu(config.WINDOW)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                menu = False

    run: bool = True

    config.clock = pygame.time.Clock()

    move_interval = 200
    pygame.time.set_timer(SNAKE_MOVE, move_interval)

    # main game loop
    sound_on = True
    while run:
        config.clock.tick(config.FPS)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:

                if game.game_over is True:
                    if event.key == pygame.K_RETURN:
                        game.game_over = False
                        game.reset()

                if event.key == pygame.K_SPACE and game.game_over is False:
                    game.show_pause_menu(config.WINDOW)
                    continue

                # Use settings for controls
                if event.key == settings.controls["left"]:
                    game.move_left()
                if event.key == settings.controls["right"]:
                    game.move_right()
                if event.key == settings.controls["down"]:
                    game.move_down()
                if event.key == settings.controls["up"]:
                    game.move_up()

                if event.key == pygame.K_m:
                    sound_on = not sound_on
                    config.music_c.set_volume(0.3 if sound_on else 0)
                    config.crunch_c.set_volume(1 if sound_on else 0)

            if event.type == SNAKE_MOVE:
                game.update()

            if event.type == UPDATE_SCORE:
                game.update_score()

        if game.game_over:
            game.show_game_over(config.WINDOW)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    game.reset()
                    break
            continue

        if game.score and game.score % 10 == 0:
            move_interval = max(50, 200 - (game.score // 10) * 10)
            pygame.time.set_timer(SNAKE_MOVE, move_interval)

        game.draw(config.WINDOW)

    pygame.quit()
    sys.exit()


def main(args):
    """Main"""
    try:
        snake(args)
    except KeyboardInterrupt:
        print("Keyboard Interrupt...")
        print("Exiting")
