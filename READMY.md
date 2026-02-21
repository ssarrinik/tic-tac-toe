# ⭕❌ Tic-Tac-Toe with Minimax AI

A command-line Tic-Tac-Toe game written in Python, featuring an unbeatable AI opponent powered by the classic Minimax algorithm. 

## 🌟 Features
* **Two Game Modes:** * Player vs. Player (Local Multiplayer)
  * Player vs. Unbeatable AI
* **Smart AI:** The Bot uses the Minimax algorithm to calculate all possible future game states. It will always force a draw or win—it cannot be beaten!
* **Dynamic Board:** Clean command-line interface that updates the board in real-time.

## 🚀 How to Run

### Prerequisites
* Python 3.x installed on your machine. No external libraries or dependencies are required.

### Execution
1. Clone this repository or download the source code.
2. Open your terminal or command prompt.
3. Navigate to the folder containing the game files.
4. Run the main Python script:

### Speed
With maxing alone the first move which is the most heavy with to a 3 by 3 matrix has execution time of 2.6s. In the
second version with alfa-beta pruning we accomplished execution time of 0.15s therefore we made it 17.34 times faster.
To activate alfa-beta pruning just go to the method play and uncomment the line and comment the other.
Even with pruning a 4 by 4 matrix we have to make 16! checkups which in my computer it will take forever.

   ```bash
   python game.py