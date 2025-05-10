# Physics Game

This is a simple physics-based platformer game built using Python and the `pygame` library. The game involves controlling a player character to jump between platforms while avoiding falling off the screen. The game features basic physics for movement, gravity, and collision detection.

## Features

- **Player Movement**: Move left, right, and jump using keyboard controls.
- **Gravity**: The player is affected by gravity, making the gameplay more realistic.
- **Collision Detection**: The player can land on platforms and interact with them.
- **Scrolling Platforms**: Platforms scroll as the player moves upward, and new platforms are generated dynamically.
- **Score System**: The score is based on the maximum height reached by the player.
- **Game Over**: The game ends if the player falls off the screen.

## Project Structure

. ├── game.py # Main game logic ├── physics_engine/ # Physics engine components │ ├── __init__.py # Marks the directory as a Python package │ ├── collision.py # Collision detection functions │ ├── particle.py # Particle class for simple physics objects │ ├── rigid_body.py # RigidBody class for rectangular objects ├── requirements.txt # Dependencies for the project ├── .gitignore # Git ignore file └── .idea/ # PyCharm project settings (ignored by Git)


### Key Files

- **[game.py](game.py)**: Contains the main game loop, player and platform logic, and rendering.
- **[physics_engine/particle.py](physics_engine/particle.py)**: Implements the `Particle` class for simple physics objects.
- **[physics_engine/rigid_body.py](physics_engine/rigid_body.py)**: Implements the `RigidBody` class for rectangular objects with physics properties.
- **[physics_engine/collision.py](physics_engine/collision.py)**: Provides collision detection functions for circles and axis-aligned bounding boxes (AABB).

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd physics_game


2. Install the required dependencies:
    pip install -r requirements.txt



## How to Play

# 1. Run the game:
    python game.py


# 2. Use the following controls:

Left Arrow: Move left
Right Arrow: Move right
Up Arrow: Jump (only when on a platform)

# 3. The objective is to jump between platforms and reach the highest possible score. Avoid falling off the screen!

## Dependencies
pygame: For rendering graphics and handling input.
numpy: For vector and matrix operations.

Install these dependencies using the requirements.txt file.

## Future Improvements

Add more platform types (e.g., moving platforms, disappearing platforms).
Introduce obstacles or enemies.
Add sound effects and background music.
Implement a high-score system.
