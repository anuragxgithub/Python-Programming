'''
NOTE: Both *args and **kwargs allows us to pass arbitrary number of arguments in 

Keyword Arguments (kwargs):
The special syntax **kwargs allows us to pass any number of keyword arguments (arguments in the form key=value).
These arguments unlike args are collected into a dictionary, where:
Keys = argument names
Values = argument values
'''

# Question: Create a function that accepts any number of keyword
# arguments and prints them in the format key: value
def experimenting(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(i)
    for k,v in kwargs.items():
        print(f"{k}: {v}", end =" ")



# experimenting(name= "anurag", roll= 10, location="Khalilabad")
experimenting(name= "anurag", power="lazer", location="Khalilabad", state="UP")
