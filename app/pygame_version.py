"""PyGame version of the fidget spinner animation.

The player can flick the spinner by pressing the space bar.

Typical usage example:

    python app/pygame_version.py
"""

import sys
import math
import pygame
from app.config import config

# Define customizable properties
WINDOW_SIZE = config["window_width"]
DOT_SIZE = config["spinner_dot_size"]
LINE_WIDTH = config["line_width"]
SPIN_INCREMENT = config["flick_turns_increment"]
ANIMATION_DELAY = config["animation_interval"]

# Initialize PyGame
pygame.init()

# Set up the PyGame window
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Spinning Animation")

# Set initial state
state = {"turn": 0}

# Define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
colors = [RED, GREEN, BLUE]


def draw_spinner(surface, angle):
    """Draws the fidget spinner.

    Args:
        screen (pygame.Surface): The PyGame screen.
        angle (int): The angle of the spinner.
    """
    surface.fill(WHITE)

    for i, color in enumerate(colors):
        x_axis = int(WINDOW_SIZE / 2 + 100 * math.cos(math.radians(angle + i * 120)))
        y_axis = int(WINDOW_SIZE / 2 + 100 * math.sin(math.radians(angle + i * 120)))
        pygame.draw.circle(screen, color, (x_axis, y_axis), DOT_SIZE // 2)

    pygame.draw.circle(
        surface, BLACK, (WINDOW_SIZE // 2, WINDOW_SIZE // 2), DOT_SIZE // 2, LINE_WIDTH
    )


def main():
    """Runs the PyGame version of the fidget spinner animation."""
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            state["turn"] += SPIN_INCREMENT

        if state["turn"] > 0:
            state["turn"] -= 1

        draw_spinner(screen, state["turn"])

        pygame.display.flip()
        clock.tick(1000 // ANIMATION_DELAY)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
