# 🎲 Dice Game

A console-based dice game written in Python.

Challenge the computer, roll the dice, earn points, and save your results for future games.

---

## 🚀 Features

* 🎯 Three difficulty levels:

  * Short (5 rounds)
  * Medium (8 rounds)
  * Long (10 rounds)

* 🎲 Random dice rolls

* 📊 Score calculation system

* 🔄 Automatic re-roll on draw

* 💾 Saving results to JSON

* 📜 Viewing previous game results

* ⚠️ Custom exception handling

* 🏗️ Object-Oriented Programming (OOP)

---

## 🎮 How to Play

1. Enter your name.
2. Select a game mode.
3. Press **Enter** to roll the dice.
4. Compete against the computer.
5. Receive your final score.
6. Save the result automatically.

---

## 📊 Scoring Rules

If the player's dice value is higher:

Player score increases by the difference.

Example:

Player: 6
Computer: 3

Difference = 3

Score = Score + 3

If the computer's dice value is higher:

Player score decreases by the difference.

Example:

Player: 2
Computer: 5

Difference = 3

Score = Score - 3

If both values are equal:

The dice are rolled again.

---

## 📁 Project Structure

```text
Dice_Game/
│
├── main.py
│
├── game/
│   ├── game.py
│   ├── models.py
│   ├── settings.py
│   ├── score.py
│   └── exceptions.py
│
├── results.json
└── README.md
```

---

## 🛠 Technologies

* Python 3
* JSON
* OOP
* Exception Handling
* Random Module

---

## 💾 Example Result

```text
Date: 2026-06-07 00:01:34
Name: John
Number of rounds: 5
Final score: 6
---------------------------------
```

---

## 🎯 Learning Goals

This project demonstrates:

* Classes and inheritance
* File handling
* JSON serialization
* Exception handling
* Program structure
* Working with modules

---

## 👨‍💻 Author

Dima Pokidčenko
Python Module 2 Project
