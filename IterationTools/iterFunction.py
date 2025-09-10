list = [1,2,4,6]
I = iter(list)
print(I)  # this I will basically hold the first object of the the list(iterable) and keep holding it always

print(I.__next__())

print(I) # see it will always point to the first object of the list(iterable)

print(I.__next__())
print(I.__next__())
print(I.__next__())

# print(I.__next__())  # will give StopIteration Error