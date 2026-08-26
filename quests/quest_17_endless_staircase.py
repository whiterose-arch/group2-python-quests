#!/usr/bin/python3
"""
Quest 17: The Endless Staircase
===============================
Level: Level 4: The Power of Repetition

Concept
-------
while loop - repeats code as long as a condition is true.

Why it matters
--------------
Perfect for when you don't know how many repetitions you need.

Logical reasoning
------------------
While this condition is true, keep executing this block of code.

The Quest (task)
-----------------
Start a counter at 0. Use a while loop that stops when the count reaches 5.

Assigned to : Emmanuel Adekojo
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_17_endless_staircase.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

count = 0
while count < 5:
    print(f"I am on step {count}")
    count += 1