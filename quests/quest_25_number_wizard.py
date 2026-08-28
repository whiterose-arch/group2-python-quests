"""
Quest 25: The Number Wizard
===========================
Level: Level 6: The Grand Challenge

The Quest: Upgrade your number guessing game. After each wrong guess, tell the user if their guess was "too high" or "too low".

Assigned to : <fill in your name>
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_25_number_wizard.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

guessed_number = int(input("Guess a number between 1 and 100: "))  # Prompt the user to guess a number and convert it to an integer

while guessed_number != 42:  # Continue looping until the user guesses the correct number (42)
    if guessed_number < 42:  # Check if the guessed number is less than the target number
        print("Too low! Try again.")  # Inform the user that their guess is too low
    else:  # If the guessed number is not less than the target number, it must be greater
        print("Too high! Try again.")  # Inform the user that their guess is too high
    guessed_number = int(input("Guess a number between 1 and 100: "))  # Prompt the user to guess again and convert it to an integer
print("Congratulations! You've guessed the correct number!")  # Inform the user that they have guessed
