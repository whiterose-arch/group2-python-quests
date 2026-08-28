#!/usr/bin/python3
"""
Quest 20: The Even Number Forager
=================================
Level: Level 4: The Power of Repetition

Concept
-------
Using if inside a for loop.

Why it matters
--------------
This lets you process items in a sequence and make a decision about each one.

Logical reasoning
------------------
For each number in this range, check if it meets my condition. If it does, perform an action.

The Quest (task)
-----------------
Loop through numbers 1 to 20. Use an if statement to check if the number is even. If it is, print it.

Assigned to : Ange Emmanuelle Ntsa Bineli
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_20_even_number_forager.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

#In the range below , the computer will only print every number which when divided by 2 gives 0. 
for i in range(1, 21):
        if i % 2 == 0:
                print(i)
#if any remainder, the computer will skip till the limit of the range
        else:
                 continue