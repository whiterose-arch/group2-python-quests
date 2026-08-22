"""
Quest 06: The Fortune Teller
============================
Level: Level 2: A Dialogue with the Machine

Concept
-------
input() - how to ask the user a question and get their answer.

Why it matters
--------------
This makes your programs interactive!

Logical reasoning
------------------
If I want the user to give me information, I need to use input() to pause the program and wait for their typed response.

The Quest (task)
-----------------
Ask the user for their name and quest, then print a confirmation message.

Assigned to : <fill in your name>
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_06_fortune_teller.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

user_name = input("What is your name, adventurer? ")  # Ask the user for their name and store it in a variable
user_quest = input("What is your quest? ")  # Ask the user for their quest and store it in a variable

print(f"Greetings, {user_name}! Your quest to '{user_quest}' has been noted.")  # Print a confirmation message using the user's input