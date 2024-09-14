from turtle import Turtle

# Constants for player movement and finish line
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    """
    Represents the player character in the game.
    """

    def __init__(self):
        """
        Initializes the player with the turtle shape and sets the starting position and heading.
        """
        super().__init__()
        self.shape("turtle")  
        self.penup()  
        self.go_to_start()  
        self.setheading(90)  

    def go_up(self):
        
        self.forward(MOVE_DISTANCE)  

    def go_to_start(self):
        self.goto(STARTING_POSITION)  

    def is_at_finish_line(self):
        """
        Checks if the player character has reached or passed the finish line.
        Returns:
            bool: True if player has crossed the finish line, False otherwise.
        """
        return self.ycor() > FINISH_LINE_Y  
