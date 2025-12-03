# Rock Paper Scissors - Machine Lerning Challenge

This is the boilerplate for the Rock Paper Scissors project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors

The main objective is to create a `player` function capable of playing the classic game "Rock, Paper, Scissors" against four different bots (Quincy, Abbey, Kris, and Mrugesh) and winning at least **60%** of the games against each of them.

## Strategy Used

To outperform bots, especially **Abbey** (which is capable of learning simple patterns), I implemented an algorithm based on **Markov Chains**.

* **Logic:** The bot observes the opponent's move history to detect sequential patterns.

* **Memory:** It analyzes the last `n` moves (configured in 4 steps) to predict the opponent's most likely next move.

* **Response:** Once the opponent's move is predicted, the bot plays the card that counters that prediction.

## Installation and Requirements

You need to have **Python 3.x** installed.

1. Clone this repository:

```bash
git clone https://github.com/GonzaPaez/rock-paper-scissors.git
cd rock-paper-scissors
```

## Project Structure

- RPS.py: Contains the main solution logic (player function). This is the only file that needs to be modified.

- main.py: Main file for running the game and tests.

- RPS_game.py: Contains the game logic and opponent bots (provided by the FCC).

- test_module.py: Unit tests to verify the win rate (provided by the FCC).

## How to Test Your Code

There are two ways to verify that your code works correctly:

1. Game Simulation (Manual)

You can see your bot play against a specific bot by editing the main.py file.

Open main.py and make sure you have a line similar to this to play against a specific bot (for example, Abbey):

```python
# Uncomment line below to play interactively against a bot:
play(human, abbey, 20, verbose=True)
```
Run the file:

```bash
python main.py
```

You'll see the breakdown of each game and the final win percentage on the console.

2. Run the Unit Tests

To pass the FreeCodeCamp challenge, the code must pass the automated tests that play 1000 games against each of the 4 bots.

- Open the main.py file.

- Find the last few lines of the file.

- Make sure the line that imports and runs the tests is not commented out:

```python
# Uncomment line below to run unit tests automatically
main(module='test_module', exit=False)
```

Run the file:

```bash
python main.py
```

If the solution is correct, you should see console output similar to this:

```text
test_player_vs_abbey (test_module.UnitTests) ... ok
test_player_vs_kris (test_module.UnitTests) ... ok
test_player_vs_mrugesh (test_module.UnitTests) ... ok
test_player_vs_quincy (test_module.UnitTests) ... ok

----------------------------------------------------------------------
Ran 4 tests in 8.452s

OK
```

The approximate win rates with this solution are usually:
vs Quincy: ~99%
vs Kris: ~72%
vs Mrugesh: ~84%
vs Abbey: ~64-72%
