#!/usr/bin/python3
"""
Quest 15: The Nested Riddle
===========================
Level: Level 3: The Crossroads of Logic

Concept
-------
Nested if Statements - an if statement inside another.

Why it matters
--------------
It allows for a second layer of decision-making after a first condition is met.

Logical reasoning
------------------
First, check if the user has a key. If they do, THEN check if it's the right color.

The Quest (task)
-----------------
Mini-adventure. Ask if they go 'left' or 'right'. If 'left', ask if they 'swim' or 'wait'. If they swim, they find a treasure. All other choices lead to a different outcome.

Assigned to : Emmanuel Adekojo
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_15_nested_riddle.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

direction = input("Enter 'left' or 'right': ").lower().strip()
if direction == "left":
    action = input("Enter 'swim' or 'wait': ").lower().strip()
    if action == "swim":
        print("You found a treasure!")
    else:
        print("You found a monster!")
else:
    print("You found a monster!")