"""A fidget spinner game.

The player can flick the spinner by pressing the space bar.

Typical usage example:

    fidget_spinner = FidgetSpinner()
    fidget_spinner.start()
"""

from turtle import Turtle, Screen, done
from app.config import config


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
        self.state = {"turn": 0}
        self.turtle = Turtle()
        self.screen = Screen()

    def spinner(self):
        """Draws the fidget spinner."""
        self.turtle.clear()
        angle = self.state["turn"] / 10
        self.turtle.right(angle)

        self.turtle.forward(config["forward_distance"])
        self.turtle.dot(config["spinner_dot_size"], "red")
        self.turtle.back(config["backward_distance"])
        self.turtle.right(config["spinner_angle"])

        self.turtle.forward(config["forward_distance"])
        self.turtle.dot(config["spinner_dot_size"], "green")
        self.turtle.back(config["backward_distance"])
        self.turtle.right(config["spinner_angle"])

        self.turtle.forward(config["forward_distance"])
        self.turtle.dot(config["spinner_dot_size"], "blue")
        self.turtle.back(config["backward_distance"])
        self.turtle.right(config["spinner_angle"])

        self.screen.update()

    def animate(self):
        """Animates the fidget spinner."""
        if self.state["turn"] > 0:
            self.state["turn"] -= 1

        self.spinner()
        self.screen.ontimer(self.animate, config["animation_interval"])

    def flick(self):
        """Increases the spinner's speed."""
        self.state["turn"] += config["flick_turns_increment"]

    def setup(self):
        """Sets up the turtle graphics environment."""
        self.screen.setup(
            config["window_width"],
            config["window_height"],
            config["window_x_offset"],
            config["window_y_offset"],
        )
        self.turtle.hideturtle()
        self.screen.tracer(False)
        self.turtle.width(config["turtle_width"])

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
