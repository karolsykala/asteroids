
# 🛸 Asteroids Game

This repository contains an implementation of the classic **Asteroids** game, developed as part of a guided project in the [Boot.dev](https://www.boot.dev/courses/build-asteroids-python) course. The project focuses on utilizing Python and the Pygame library to create an interactive, object-oriented game.

## 🚀 Features

- **Player Control**: Navigate the spaceship using keyboard inputs.
- **Asteroid Field**: Randomly generated asteroids that the player must avoid or destroy.
- **Shooting Mechanism**: Fire projectiles to break apart asteroids.
- **Collision Detection**: Realistic interactions between the spaceship, asteroids, and projectiles.

## 🛠️ Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/karolsykala/asteroids.git
   cd asteroids
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Install the required packages using pip:
   ```sh
   pip install -r requirements.txt
   ```

## 🎮 Usage

Run the game using:
```sh
python main.py
```
Control the spaceship with the arrow keys and shoot projectiles using the spacebar. The objective is to destroy all asteroids without colliding with them.

## 📂 Project Structure

- `main.py`: Initializes the game and contains the main game loop.
- `player.py`: Defines the Player class and handles spaceship behavior.
- `asteroid.py`: Defines the Asteroid class and manages asteroid properties.
- `asteroidfield.py`: Manages the generation and updating of multiple asteroids.
- `shot.py`: Defines the Shot class for the projectiles fired by the player.
- `circleshape.py`: Contains a base class for circular game objects.
- `constants.py`: Stores game-wide constants such as screen dimensions and colors.

