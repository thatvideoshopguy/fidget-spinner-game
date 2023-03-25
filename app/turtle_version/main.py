"""A fidget spinner game.

The player can flick the spinner by pressing the space bar.

Typical usage example:

    fidget_spinner = FidgetSpinner()
    fidget_spinner.start()
"""

from turtle import Turtle, Screen, done
from .config import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    WINDOW_X_OFFSET,
    WINDOW_Y_OFFSET,
    SPINNER_DOT_SIZE,
    TURTLE_WIDTH,
    ANIMATION_INTERVAL,
    FLICK_TURN_INCREMENT,
    FORWARD_DISTANCE,
    BACKWARD_DISTANCE,
    SPINNER_ANGLE,
)


class FidgetSpinner:
    """A fidget spinner game.

    The player can flick the spinner by pressing the space bar.

    Attributes:
        state (dict): The game state.
        turtle (Turtle): The turtle object.
        screen (Screen): The screen object.
    """

    def __init__(self):
        """Initializes the game."""
        self.state = {"rotation_speed": 0}
        self.turtle = Turtle()
        self.screen = Screen()

    def spinner(self):
        """Draws the fidget spinner."""
        self.turtle.clear()
        angle = self.state["rotation_speed"] / 10
        self.turtle.right(angle)

        colors = ["red", "green", "blue"]

        for color in colors:
            self.turtle.forward(FORWARD_DISTANCE)
            self.turtle.dot(SPINNER_DOT_SIZE, color)
            self.turtle.back(BACKWARD_DISTANCE)
            self.turtle.right(SPINNER_ANGLE)

        self.screen.update()

    def animate(self):
        """Animates the fidget spinner."""
        if self.state["rotation_speed"] > 0:
            self.state["rotation_speed"] -= 1

        self.spinner()
        self.screen.ontimer(self.animate, ANIMATION_INTERVAL)

    def flick(self):
        """Increases the spinner's speed."""
        self.state["rotation_speed"] += FLICK_TURN_INCREMENT

    def configure_turtle(self):
        """Configures the turtle object."""
        self.turtle.hideturtle()
        self.screen.tracer(False)
        self.turtle.width(TURTLE_WIDTH)

    def setup(self):
        """Sets up the turtle graphics environment."""
        self.screen.setup(
            WINDOW_WIDTH,
            WINDOW_HEIGHT,
            WINDOW_X_OFFSET,
            WINDOW_Y_OFFSET,
        )
        self.configure_turtle()

    def register_events(self):
        """Registers event handlers."""
        self.screen.onkey(self.flick, "space")
        self.screen.listen()

    def start(self):
        """Starts the fidget spinner game."""
        self.setup()
        self.register_events()
        self.animate()
        done()


def main():
    """Starts the fidget spinner game."""
    fidget_spinner = FidgetSpinner()
    fidget_spinner.start()


if __name__ == "__main__":
    main()
