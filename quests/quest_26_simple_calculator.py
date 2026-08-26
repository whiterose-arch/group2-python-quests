#!/usr/bin/python3
"""
Quest 26: The Simple Calculator
===============================
Level: Level 6: The Grand Challenge

The Quest: Write a program that acts as a simple calculator. Ask for two numbers and an operation (add, subtract, etc.). Use functions for each operation and an if-elif-else chain to call the correct one.

Assigned to : Emmanuel Adekojo
Group       : group2-python-quests
Status      : [ ] not started  [ ] in progress  [ ] done  [ ] reviewed by peers
"""

# ---------------------------------------------------------------------------
# Write your solution below this line.
# Remember: keep it simple, test it by running `python quest_26_simple_calculator.py`,
# and add short inline comments (#) explaining tricky lines before you push.
# ---------------------------------------------------------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator(a, b, operation):
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
      if b == 0:
          return "Syntax error"
      return divide(a, b)

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").lower().strip()

if operation not in ["add", "subtract", "multiply", "divide"]:
    print("Invalid operation")
else:
  result = calculator(number1, number2, operation)
  print(f"The result of {number1} {operation} {number2} is {result}")