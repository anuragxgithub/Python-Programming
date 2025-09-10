name = "Anurag"

def func():
    # name = "Rahul"
    print(name)

print(name)
func()

x = 99
def func2(y):
    z = x+y
    return z

print(func2(1))

# 3 USING 'global' KEYWORD
l = 99
def func3():
    global l
    l = 69
    return l

func3()
print(l)


# NOTE: Avoid using global variables