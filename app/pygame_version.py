"""PyGame version of the fidget spinner animation.

The player can flick the spinner by pressing the space bar.

Typical usage example:

    python app/pygame_version.py
"""

import sys
import math
import pygame
import pygame.gfxdraw
from app.config import config


class FidgetSpinnerGame:
    """A fidget spinner game.

    The player can flick the spinner by pressing the space bar.

    Attributes:
        state (dict): The game state.
        colors (list): The colors of the spinner.
        screen (Screen): The screen object.
    """

    def __init__(self):
        """Initialize the game and create a PyGame window."""
        self.state = {
            "rotation_angle": 0,
            "rotation_direction": 0,
            "rotation_acceleration": 0,
        }
        self.colors = [config["red"], config["green"], config["blue"]]

        pygame.init()
        self.screen = pygame.display.set_mode(
            (config["window_width"], config["window_width"])
        )

        pygame.display.set_caption("Spinning Animation")

    def draw_spinner(self, angle):
        """Draws the fidget spinner.

        Args:
            angle (int): The angle of the spinner.
        """
        self.screen.fill(config["white"])

        center_x = config["window_width"] // 2
        center_y = config["window_width"] // 2
        line_width_half = config["line_width"] // 2

        for i, color in zip(range(0, 360, 120), self.colors):
            x_axis = int(center_x + 100 * math.cos(math.radians(angle + i)))
            y_axis = int(center_y + 100 * math.sin(math.radians(angle + i)))

            direction_x = x_axis - center_x
            direction_y = y_axis - center_y
            dist = math.sqrt(direction_x * direction_x + direction_y * direction_y)
            direction_x /= dist
            direction_y /= dist

            offset_x = line_width_half * direction_y
            offset_y = line_width_half * direction_x

            pygame.gfxdraw.filled_polygon(
                self.screen,
                [
                    (center_x - offset_x, center_y + offset_y),
                    (center_x + offset_x, center_y - offset_y),
                    (x_axis + offset_x, y_axis - offset_y),
                    (x_axis - offset_x, y_axis + offset_y),
                ],
                config["black"],
            )

            radius = config["spinner_dot_size"] // 2
            pygame.gfxdraw.filled_circle(self.screen, x_axis, y_axis, radius, color)
            pygame.gfxdraw.aaellipse(self.screen, x_axis, y_axis, radius, radius, color)

    def update_game_state(self):
        """Updates the game state."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.state["rotation_acceleration"] += config[
                "flick_acceleration_increment"
            ]
            self.state["rotation_direction"] = (
                1 if self.state["rotation_acceleration"] >= 0 else -1
            )
        else:
            self.state["rotation_acceleration"] -= config[
                "flick_deceleration_increment"
            ]
            if self.state["rotation_acceleration"] < 0:
                self.state["rotation_acceleration"] = 0

        self.state["rotation_angle"] += (
            self.state["rotation_direction"] * self.state["rotation_acceleration"]
        )

    def run(self):
        """Runs the PyGame version of the fidget spinner animation."""
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update_game_state()
            self.draw_spinner(self.state["rotation_angle"])

            pygame.display.flip()
            clock.tick(1000 // config["animation_interval"])


def main():
    """The main function."""
    fidget_spinner_game = FidgetSpinnerGame()
    fidget_spinner_game.run()


if __name__ == "__main__":
    main()
