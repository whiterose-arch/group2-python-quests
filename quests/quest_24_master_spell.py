#!/usr/bin/python3
"""
Quest 24: The Master Spell
==========================
Level: Level 5: The Alchemist's Lab

Concept
-------
Calling a function from within another function.

Why it matters
--------------
This is how you build complex programs from simple, reusable parts.

Logical reasoning
------------------
I can break a big problem down into smaller tasks. Each task becomes a function.

The Quest (task)
-----------------
Create ask_for_age() which returns an age, and can_they_vote(age) which prints a message. Call the first, then pass its result to the second.

Assigned to : <fill in your name>
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_24_master_spell.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

def ask_for_age():
        age = int(input("what is your age: "))
        return(age)
        print(f"your age is {age}")
def can_they_vote(age):
        if age > 10:
                return f"yes, {age} can vote"
        else:
                return f"no, {age} can't vote"