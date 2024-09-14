

# Turtle Crossing The Road

## Overview
This is the day 23 project of the course 100 Days of Code: The Complete Python Pro Bootcamp. This project involves creating a simple game where a turtle (the player) must cross a road filled with moving cars while avoiding collisions. 

## Files

### 1. `car_manager.py`
Handles the creation, movement, and management of cars in the game. Cars are represented as squares with varying colors and speeds. The `CarManager` class includes methods to:
- Create new cars with random attributes.
- Move all cars across the screen.
- Increase car speed as the game progresses.

### 2. `player.py`
Defines the player character (a turtle) and its movements. The `Player` class allows the turtle to:
- Move up the screen.
- Reset to the starting position.
- Check if it has reached the finish line.

### 3. `scoreboard.py`
Manages and displays the game's score and level. The `Scoreboard` class:
- Shows the current level.
- Updates the score when the player crosses the finish line.
- Displays a game over message when a collision occurs.

### 4. `main.py`
The entry point of the game that sets up the screen, creates game objects, and runs the main game loop. It includes:
- Screen setup and updates.
- Keyboard controls for player movement.
- Game loop logic to handle car creation, movement, collision detection, and level progression.

## Gameplay
In this game, you control a turtle that needs to cross a busy road filled with moving cars. Use the "Up" arrow key to move the turtle forward. Avoid collisions with the cars and try to reach the finish line to level up. As you progress, the speed of the cars will increase.

## Requirements

- Python 3.x
- `turtle` module (comes pre-installed with Python)

## **Example**

![alt text]()
