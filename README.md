# 🏏 Mini Cricket
A simple command-line cricket game built using Python.
The project is designed as a small hands-on project to practice Python programming fundamentals.
---
## 🎯 Project Goal
Build a simple cricket game that can be played from the terminal.
The player can:
- Configure a match
- Choose a batting strategy
- Play ball by ball
- Score runs
- Lose wickets
- Track balls and overs
- Chase a target score
- See the final match summary
The project starts with simple functions and gradually separates responsibilities into different modules.
---
## 🎮 Game Overview
At the beginning of the match, the player enters:
- Number of overs
- Number of wickets
- Target score
For every ball, the player chooses a batting strategy:
1. Defensive
2. Normal
3. Aggressive
The game then randomly generates the outcome of the shot.
Possible outcomes are:
- `0`
- `1`
- `2`
- `3`
- `4`
- `6`
- `W` (Wicket)
The innings ends when one of the following happens:
- Target score is reached
- All wickets are lost
- All available balls are completed
---
## 🧠 Batting Strategies
### 1. Defensive
Focuses on reducing the chance of losing a wicket.
Possible outcomes:
```text
0, 0, 1, 1, 2, 4
```
## 🛠️ Tech Stack
- Python 3
- Command Line / Terminal
- Python Standard Library
- Git
No external Python dependencies are required.
## 📋 Requirements
Before running the project, make sure the following are installed on your system:
#### Python 3
Check whether Python 3 is installed:
```bash
python3 --version

Example output:
Python 3.12.0
```
If Python 3 is not installed, install it from the official Python website.
#### Git
Git is required to clone the repository and manage the project history.
Check whether Git is installed:
```bash
git --version
```
Example output:
```
git version 2.50.0
```
---
## 🚀 Getting Started
Follow these steps to run Mini Cricket locally.
### 1. Clone the Repository
Clone the repository using Git:
```bash
git clone https://github.com/priyanshverma11/mini-cricket.git
```
### 2. Navigate to the Project Directory
```bash
cd mini-cricket
```
### 3. Verify the Project Structure
The project should have the following structure:
```text
mini-cricket/
├── README.md
└── src/
    ├── main.py
    ├── game.py
    └── display.py
```
### 4. Run the Game
Run the application from the project root directory:
```bash
python3 -m src.main
```
### 5. Start Playing
The game will ask you to configure the match:
```text
Enter number of overs: 2
Enter number of wickets: 2
Enter target score: 10
```
You can then choose your batting strategy for each ball:
```text
Choose your shot:
1. Defensive
2. Normal
3. Aggressive
Enter choice:
```
---
🎯 Example Gameplay

- ================================
-        🏏 MINI CRICKET
- ================================
- Enter number of overs: 2
- Enter number of wickets: 2
- Enter target score: 10
- Overs   : 2
- Wickets : 2
- Target  : 10
- Choose your shot:
1. Defensive
2. Normal
3. Aggressive
- Enter choice: 2
📋
- Ball 1: 🏏 4 run(s)

Score : 4/0
Overs : 0.1

The game continues until the target is reached, all wickets are lost, or the configured number of overs is completed.

## 🧩 Python Concepts Practiced
This project currently covers:
- Variables
- Data types
- Functions
- Function parameters and return values
- Type hints
- Conditional statements
- while loops
- Lists
- Sets
- Dictionaries
- Random number generation

## VS CODE Output Image
<img width="480" height="658" alt="image" src="https://github.com/user-attachments/assets/81badb44-924d-4084-abc4-b28f8489b76e" />
