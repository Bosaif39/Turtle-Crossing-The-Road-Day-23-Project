from turtle import Turtle
import random

# Constants for car colors and movement
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    """
    Manages the cars in the game, including their creation, movement, and speed.
    """

    def __init__(self):
        """
        Initializes the CarManager with an empty list of cars and sets the initial car speed.
        """
        self.all_cars = []  
        self.car_speed = STARTING_MOVE_DISTANCE  

    def create_car(self):
        """
        Randomly creates a new car and adds it to the list of cars.
        The chance of creating a car is 1 in 6.
        This reduce the number of cars so the game will be fair.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")  
            new_car.shapesize(stretch_wid=1, stretch_len=2)  
            new_car.penup()  
            new_car.color(random.choice(COLORS))  
            random_y = random.randint(-250, 250)  
            new_car.goto(300, random_y)  # Position the car on the right side of the screen
            self.all_cars.append(new_car)  

    def move_cars(self):
        """
        Moves all cars backward based on the current car speed.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)  

    def level_up(self):
        """
        Increases the speed of the cars by a predefined increment.
        """
        self.car_speed += MOVE_INCREMENT  
