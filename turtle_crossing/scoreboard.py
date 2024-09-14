from turtle import Turtle

# Font settings for scoreboard text
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """
    Displays and updates the player's score and game status.
    """

    def __init__(self):
        """
        Initializes the scoreboard with the starting level and positions it on the screen.
        """
        super().__init__()
        self.level = 1  # Starting level
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Prevent drawing while moving
        self.goto(-280, 250)  # Position the scoreboard
        self.update_scoreboard()  # Display the initial score

    def update_scoreboard(self):
        """
        Updates the scoreboard display to show the current level.
        """
        self.clear()  # Clear previous text
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Write the current level

    def increase_level(self):
        """
        Increases the level by 1 and updates the scoreboard.
        """
        self.level += 1  # Increment the level
        self.update_scoreboard()  # Refresh the scoreboard display

    def game_over(self):
        """
        Displays a game over message on the scoreboard.
        """
        self.goto(0, 0)  # Move to the center of the screen
        self.write(f"GAME OVER", align="center", font=FONT)  # Write game over message
