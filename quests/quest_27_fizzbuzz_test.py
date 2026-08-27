#!/usr/bin/python3
"""
Quest 27: The FizzBuzz Test
===========================
Level: Level 6: The Grand Challenge

The Quest: A classic challenge. Print numbers from 1 to 100. For multiples of 3, print "Fizz". For multiples of 5, print "Buzz". For multiples of both, print "FizzBuzz".

Assigned to : Ange Emmanuelle Ntsa Bineli
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_27_fizzbuzz_test.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz", i)
        elif i % 3 == 0:
                print("Fizz", i)

        elif i % 5 == 0:
                print("Buzz", i)
        else:
                print(i)
