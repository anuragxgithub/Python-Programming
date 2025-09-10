f = open('iteration_tool.py')

# print(f.readline())


# for line in f:
#     print(line, end="")


while True:
    line = f.readline()
    if not line: break
    print(line, end="")

# print(f.read())


# Note: this will only work if you run it from the same location/folder from where
# it is created (also where iteration_too.py is present)