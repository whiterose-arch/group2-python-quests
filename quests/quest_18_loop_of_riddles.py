"""
Quest 18: The Loop of Riddles
=============================
Level: Level 4: The Power of Repetition

Concept
-------
Using a while loop with a user-input condition.

Why it matters
--------------
It's the basis for games, user menus, and data processing.

Logical reasoning
------------------
I will keep repeating this action until the user provides the correct input to stop the loop.

The Quest (task)
-----------------
Write a guessing game. Think of a secret number. Use a while loop to keep asking the user to guess until they get it right.

Assigned to : <fill in your name>
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_18_loop_of_riddles.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

guessed_number = int(input("Guess a number between 1 and 10: "))  # Prompt the user to guess a number and convert it to an integer

while guessed_number != 4:  # Continue looping until the user guesses the correct number (4)

    print("Wrong! Try again.")  # Inform the user that their guess is too high
    guessed_number = int(input("Guess a number between 1 and 10: "))  # Prompt the user to guess again and convert it to an integer
print("Congratulations! You've guessed the correct number!")  # Inform the user that they have guessed