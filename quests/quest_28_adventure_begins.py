"""
Quest 28: The Adventure Begins
==============================
Level: Level 6: The Grand Challenge

The Quest: Create a text-based "Choose Your Own Adventure" game. Use functions for different locations and have at least two different endings.

Assigned to : Eric Mugisha
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_28_adventure_begins.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

# TODO: implement the quest here
def forest():
    print("You are in a forest.")
    choice = input("Do you go left (1) or right (2)? (1 or 2) ")

    if choice == "1":
        print("You find a treasure! You win!")
    else:
        print("You meet a scary wolf! Game over!")


def cave():
    print("You are in a dark cave.")
    choice = input("Do you go inside (1) or leave (2)? (1 or 2) ")

    if choice == "1":
        print("You find a hidden room! You win!")
    else:
        print("You leave the cave safely. Game over!")


def start_game():
    print("Welcome to the Adventure Game!")
    print("You see a forest and a cave.")

    choice = input("Do you choose the forest (1) or cave (2)? (1 or 2) ")

    if choice == "1":
        forest()
    elif choice == "2":
        cave()
    else:
        print("That is not a choice. Game over!")


start_game()
