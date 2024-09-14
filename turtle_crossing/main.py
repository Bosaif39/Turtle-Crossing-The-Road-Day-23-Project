import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Define the size of the game window
screen.tracer(0)  # Turn off screen updates for smoother animation

# Create game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkey(player.go_up, "Up")  # Move player up when 'Up' key is pressed

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Control the game speed
    screen.update()  # Update the screen

    car_manager.create_car()  # Create new cars
    car_manager.move_cars()  # Move existing cars

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False  # End the game if collision is detected
            scoreboard.game_over()  # Display game over message

    # Detect successful crossing of finish line
    if player.is_at_finish_line():
        player.go_to_start()  # Reset player position
        car_manager.level_up()  # Increase car speed
        scoreboard.increase_level()  # Update level on scoreboard

# Close the game window on click
screen.exitonclick()
