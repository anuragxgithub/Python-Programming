'''
In Python, every object has a truthy or falsy value when used in a condition.
Falsy values (treated as False):

0 (integer, float, complex zero)
"" (empty string)
[] (empty list)
{} (empty dict)
() (empty tuple)
set() (empty set)
None
False itself

Truthy values: Almost everything else (non-empty strings, non-zero numbers, non-empty collections, objects, etc.).
'''

# not is used to reverse the true value as we know

# We we will see how we can 'not' inside if condition
name = "anurag"
if not name:   # an empty string in python is treated as false
    print("name is an empty string")
else:
    print("name is not an empty string")

str = ""
if not str:       # str -> false and not is making it true
    print("Hello!!")