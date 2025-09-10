# In python we can pass variable number of arguments in a function by using *args

def learningAboutArgs(*args):                 # NOTE: in place of args we can write any name but by convention we write args
    print(args)   # See it is storing items in tuple internally
    # so that means we can do this

    for items in args:
        print(items, end=" ")


learningAboutArgs(1,2,3,4,5)
print()


# Now, QUESTION: Write a function that takes variable number of arguments and return their sum

def sum_all(*args):
    # return sum(args)        # this is one method for adding all numbers (using in-built sum() function)
    sum = 0;
    for n in args:
        sum += n
    return sum



print(sum_all(1,2,3,34,4,5,54,4))
