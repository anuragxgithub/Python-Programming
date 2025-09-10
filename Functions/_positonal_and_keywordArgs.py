'''
1. Positional Arguments
These are arguments that are matched to parameters by their position/order.
The order in which you pass them must match the order of parameters in the function definition.
✅ Example:
'''

def greet(name, age):
    print(f"Hello {name}, you are {age} years old")

# Passing arguments by position
greet("Anurag", 20)   # name="Anurag", age=20

# NOTE: If you change the order:

greet(20, "Anurag")  
# name=20, age="Anurag" (wrong meaning!)




'''
2. Keyword Arguments

These are arguments that are passed with the parameter name explicitly.
Order doesn’t matter since you specify which parameter gets which value.
✅ Example:
'''

def greet(name, age):
    print(f"Hello {name}, you are {age} years old")

# Passing arguments by keyword
greet(age=20, name="Anurag")  


# This works fine even though the order is swapped.