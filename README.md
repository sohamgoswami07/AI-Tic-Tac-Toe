# Tic Tac Toe Game vs AI Agent

This is a simple web-based Tic Tac Toe game built using Django and Python, where you can play against an AI agent. The AI is designed using a basic algorithm that makes intelligent moves for an engaging gameplay experience.

---

## Features

- **Play against AI**: Challenge the AI agent, which uses a simple minimax algorithm to decide its moves.
- **Web Interface**: A user-friendly web interface built with Django.
- **Game History**: The game keeps track of the game state, including win/loss/draw, allowing users to restart and play multiple rounds.
- **Responsive Design**: The game is responsive and works on both desktop and mobile devices.

---

## Prerequisites

To run this project locally, you'll need the following:

- **Python** (3.6+)
- **Django** (latest version)
- **pip** (Python package manager)

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sohamgoswami07/Tic-Tac-Toe-AI-Agent.git
   cd tic_tac_toe
   ```

2. **Set up a Virtual Environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   # On Mac use source `venv/bin/activate`
   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   Install the required packages listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Django Development Server**:

   Run the development server to start the game.

   ```bash
   python manage.py runserver
   ```

5. **Open the Game**:

   Navigate to `http://127.0.0.1:8000` in your web browser, and you can start playing the Tic Tac Toe game.

---

## How the AI Works

The AI in this project uses a **Minimax Algorithm** for decision-making. This algorithm explores all possible game states and chooses the best move based on the assumption that the opponent will also play optimally. It evaluates each potential board state, with the goal of either maximizing its own chances of winning or minimizing the chances of the player winning.

---

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and make improvements. Here's how you can contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes.
4. Commit your changes: `git commit -am 'Add feature'`
5. Push to your branch: `git push origin feature-name`
6. Create a new pull request.

---

## License

Created and developed by Soham Goswami.

---

## Acknowledgments

- **Django** for the web framework.
- **Python** for the backend logic and AI algorithms.
- **Minimax Algorithm** for the AI agent's decision-making.
  
---
