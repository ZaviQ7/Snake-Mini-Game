# Python Snake Mini-Game

An enhanced version of the classic Snake game built with Python and Pygame. This project features a full graphical user interface (GUI) menu, configurable game settings, visual themes, and session high score tracking.

## Features

*   **Interactive GUI Menu:** A full start screen to control all settings before playing.
*   **Configurable Difficulty:** Choose between Slow, Normal, and Fast snake speeds directly from the menu.
*   **Configurable Block Size:** Select Small, Medium, or Large block sizes to change the game's look and challenge.
*   **Light & Dark Themes:** Instantly switch between a sleek dark mode and a clean light mode.
*   **Session High Score:** The game tracks and displays the highest score achieved since the program was launched.
*   **Automatic Fullscreen:** The game launches in an immersive, borderless fullscreen mode.
*   **Classic, Responsive Gameplay:** Core snake mechanics are smooth and bug-free.

## How to Run

### Prerequisites

*   Python 3.x
*   pip (Python package installer)

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ZaviQ7/Snake-Mini-Game.git
    cd Snake-Mini-Game
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    # Create and activate a virtual environment (optional but recommended)
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    # Install the required packages
    pip install -r requirements.txt
    ```

3.  **Run the game:**
    ```bash
    python main.py
    ```

## Controls

### In-Game
*   **Arrow Keys**: Control the direction of the snake.

### Menu & Game Over Screen
*   **Mouse Click**: Select difficulty, block size, start the game, or toggle the theme.
*   **C Key**: Play Again (from the "Game Over" screen).
*   **Q Key**: Quit the game (from the "Game Over" screen).
*   **ESC Key**: Quit the game from any screen at any time.
