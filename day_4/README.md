# Rock, Paper, Scissors Game

This Python program is a text-based implementation of the classic **Rock, Paper, Scissors** game. Players compete against the computer, and the program determines the winner based on user and computer choices.

## Day 4: Concepts Learned

On the fourth day of my Python learning journey, I explored and applied the following concepts:

1. **Random Module**:
   - Learned how to use the `random` module for generating random choices.
   - Understood the concept of offsets while using randomness.

2. **Lists**:
   - Explored the concept of lists in Python for storing multiple items.
   - Learned how to append items to lists dynamically.

3. **Index Errors**:
   - Identified and understood index errors that occur when accessing invalid list indices.

4. **Nested Lists**:
   - Learned how nested lists work and how to access their elements.

5. **Project Building**:
   - Implemented all these concepts to create the **Rock, Paper, Scissors** game.

## How the Game Works

1. The user is prompted to choose between `rock`, `paper`, or `scissors`.
2. The computer makes a random selection from the same options.
3. The program compares the choices using the following rules:
   - Rock beats Scissors.
   - Scissors beats Paper.
   - Paper beats Rock.
4. The game outputs the winner and displays ASCII art representing the choices.

## Example Gameplay

```plaintext
Choose rock, paper, or scissors: rock
Your choice = 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

and 
computer's choice = 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Computer wins!

