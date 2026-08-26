#!/usr/bin/python3
"""
Quest 22: The Personalized Scroll
=================================
Level: Level 5: The Alchemist's Lab

Concept
-------
Functions with parameters (arguments).

Why it matters
--------------
This makes functions flexible. They can act on the specific data you give them.

Logical reasoning
------------------
My function needs information to do its job. I'll define 'parameters' as placeholders for that information.

The Quest (task)
-----------------
Create a function personalized_greeting(name, quest). Ask the user for their name and quest, then call your function with their answers.

Assigned to : Emmanuel Adekojo
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_22_personalized_scroll.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

def personalized_greeting(name, quest):
    print(f"Hello {name}, you are on quest {quest}")

name = input("Enter your name: ")
quest = input("Enter your quest: ")
personalized_greeting(name, quest)