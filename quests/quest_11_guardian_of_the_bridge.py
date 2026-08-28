"""
Quest 11: The Guardian of the Bridge
====================================
Level: Level 3: The Crossroads of Logic

Concept
-------
if statement - lets your program make a decision.

Why it matters
--------------
This is how programs become 'smart.' They can react differently to different situations.

Logical reasoning
------------------
If a specific condition is met, then execute the following code.

The Quest (task)
-----------------
Ask for the user's age. If it's 18 or greater, print a message that they are old enough to vote.

Assigned to : Eric Mugisha
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_11_guardian_of_the_bridge.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

age = int(input("What is your age? : "))  # Ask the user for their age and convert it to an integer

if age >= 18:
    print("You are old enough to vote!")
