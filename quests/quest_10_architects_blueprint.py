#!/usr/bin/python3
"""
Quest 10: The Architect's Blueprint
===================================
Level: Level 2: A Dialogue with the Machine

Concept
-------
Floating-Point Numbers (float) - numbers with decimal points.

Why it matters
--------------
Not all math involves whole numbers. Measurements and money often require decimals.

Logical reasoning
------------------
If my calculation might result in a fraction, I should use float to ensure the decimal part isn't lost.

The Quest (task)
-----------------
Calculate the area of a rectangle. Ask the user for the length and width (they can be decimals) and print the area.

Assigned to : Emmanuel Adekojo
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_10_architects_blueprint.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is {area}")