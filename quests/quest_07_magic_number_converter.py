#!/usr/bin/python3
"""
Quest 07: The Magic Number Converter
====================================
Level: Level 2: A Dialogue with the Machine

Concept
-------
Type Conversion - changing data from one type to another.

Why it matters
--------------
input() always gives you a string. If you want to do math, you must convert it to a number.

Logical reasoning
------------------
A computer sees '5' from an input as a word. I must tell it to reinterpret that word as a number before I can do math with it.

The Quest (task)
-----------------
Ask the user for their birth year, convert it to an integer, and calculate their approximate age.

Assigned to : Emmanuel Adekojo
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_07_magic_number_converter.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

birth_year = input("Enter your birth year: ")
age = 2026 - int(birth_year)
print(f"Your age is {age}")