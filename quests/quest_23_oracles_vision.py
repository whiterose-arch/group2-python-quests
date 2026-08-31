"""
Quest 23: The Oracle's Vision
=============================
Level: Level 5: The Alchemist's Lab

Concept
-------
Functions that return a value.

Why it matters
--------------
Many functions are designed to perform a calculation and give back the result.

Logical reasoning
------------------
This function's job is to compute a value. After it's done, it should return the final answer.

The Quest (task)
-----------------
Write a function calculate_area(length, width) that returns the area. Call it for two different rectangles and print the results.

Assigned to : Eric Mugisha
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_23_oracles_vision.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

# TODO: implement the quest here
def calculate_area(length, width):
    return length * width  # Return the product of length and width as the area

# Call the function for two different rectangles and print the results
area1 = calculate_area(5, 10) 
print(f"The area of the first rectangle is: {area1}")  # Print the area of the first rectangle

area2 = calculate_area(7, 3) 
print(f"The area of the second rectangle is: {area2}")  # Print the area