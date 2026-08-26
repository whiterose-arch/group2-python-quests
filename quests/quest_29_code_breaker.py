#!/usr/bin/python3
"""
Quest 29: The Code Breaker
==========================
Level: Level 6: The Grand Challenge

The Task: Translate the following human logic into a Python script: Allow a user 3 attempts to guess the secret code (42). Give feedback on each guess and stop the game on a correct guess or after 3 failed attempts.

Assigned to : Emmanuel Adekojo
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_29_code_breaker.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

secret_code = 42
attempts = 0
while attempts < 3:
    guess = int(input("Enter your guess: "))
    if guess == secret_code:
        print("You guessed the secret code!")
        break
    else:
        print("Wrong guess!")
    attempts += 1
if attempts == 3:
    print("You failed to guess the secret code!")