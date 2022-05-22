#!/usr/bin/python3

import pygame
import sys
import logging
from src.level import Level


class Game:
    def __init__(self):
        # Setup Pygame
        pygame.init()
        self.SCREEN = pygame.display.set_mode(
            (640, 360),
            flags=pygame.FULLSCREEN | pygame.SCALED,
            vsync=True
            )
        pygame.display.set_caption("Stella Vulpes")
        self.CLOCK = pygame.time.Clock()

        self.level = Level()

    def run(self):
        # --- GAME LOOP ---
        while True:
            # Event Loop
            for event in pygame.event.get():
                # Exit the game when clicking exit button or hitting the escape
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYUP and
                            event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    logging.info("Program End")
                    sys.exit()
                # Take a screenshot when hitting the forwared slash key
                if event.type == pygame.KEYUP and event.key == pygame.K_SLASH:
                    pygame.image.save(self.SCREEN, "screenshot.png")
                    logging.info("Screenshot saved as \"screenshot.png\"")

            # Draw stuff on screen
            self.SCREEN.fill("black")
            self.level.run()

            # Update the display and tick forward at framerate
            pygame.display.update()
            self.CLOCK.tick(60)


if __name__ == "__main__":
    # Set up debug logging
    log_format = "%(asctime)s (%(module)s.py) [%(levelname)s] %(message)s"
    logging.basicConfig(
        filename="debug.log",
        filemode="w",
        format=log_format,
        level=logging.DEBUG
        )
    logging.info("Program Start")

    try:
        game = Game()
        game.run()
    except Exception:
        logging.exception("Fatal error in main loop")
