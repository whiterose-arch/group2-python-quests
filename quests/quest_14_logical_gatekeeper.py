#!/usr/bin/python3
"""
Quest 14: The Logical Gatekeeper
================================
Level: Level 3: The Crossroads of Logic

Concept
-------
Logical Operators (and, or, not) - combine multiple conditions.

Why it matters
--------------
Real-world decisions often depend on more than one factor.

Logical reasoning
------------------
To enter the castle, you must have a key AND know the password.

The Quest (task)
-----------------
A club bouncer requires guests to be 18+ AND have 20+ gold coins. Ask the user for their age and gold, and tell them if they can enter.

Assigned to : Ange Emmanuelle Ntsa Bineli
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_14_logical_gatekeeper.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

age = int(input("what is your age: "))
gold = int(input("how many gold coins do you have: "))

if  age > 18 and gold > 20:
        print("welcome to the club")
elif age <= 18 and gold <= 20:
        print("sorry you are not welcome, you can't enter")
else:
        print("invalid age or gold")