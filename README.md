# Aim Game

**Aim Game** is a simple shooting game developed using Python and Pygame. In this game, you aim at targets that appear randomly on the screen and try to hit them before they disappear. The game keeps track of your performance, including the number of hits, misses, and your accuracy.

## Features

- Targets appear and grow on the screen.
- Click on targets to score points.
- The game tracks time, hits, misses, and calculates your shooting speed and accuracy.
- End screen with the option to replay the game.

## Installation

To run this game, you need Python and Pygame installed. You can install Pygame using pip:

```bash```
pip install pygame

# Usage
Clone the repository
git clone https://github.com/yourusername/aim-game.git
cd aim-game

Run the game
python game.py

# Gameplay
* **Controls**: Simply click on the targets that appear on the screen.
* **Objective**: Hit as many targets as you can before you run out of lives.
* **Lives**: You start with 3 lives. Each miss costs you a life.
* **Time**: The game runs for a limited time, and your performance is evaluated based on hits and misses.

# Code Explanation
Target Class
Defines the targets that appear on the screen. Targets grow and shrink over time and can be clicked to score points.

Button Class
Defines the buttons used in the game, such as the replay button on the end screen.

Main Game Loop
Manages game events, updates target positions, handles mouse clicks, and draws game elements on the screen.

# Configuration
Variables
* `TARGET_INC`: Time interval (in milliseconds) for the appearance of new targets.
* `LIVES`: Number of lives the player starts with.
* `WIDTH` and `HEIGHT`: Dimensions of the game window.

# Example
Here's a brief look at how to create and update a target:
target = Target(x, y)  # Create a new target at position (x, y)
target.update()        # Update the target's size
target.draw(win)       # Draw the target on the window

# Contributing
Feel free to fork the repository and submit pull requests with improvements or bug fixes. If you have any suggestions or issues, please open an issue on GitHub.

# Acknowledgments
* Pygame for the game development library.
* The open-source community for providing valuable tools and resources.
