'''
x = 99

def f1():
    x = 10
    def f2():
        print(x)
    f2()
f1()

Here output will be 10
'''

'''
Closure in Python:
A closure in Python is a function object that remembers the values from its enclosing scope
even after that scope has finished executing.

In simple words:
You define a function inside another function.
The inner function uses variables from the outer function.
When you return the inner function, it still "remembers" those variables, even if the
outer function has ended.
'''

x = 99

def f1():
    x = 10
    def f2():
        print(x)
    return f2    # returning the inner function

result = f1()
result()    # see the inner function also remembers the variables of enclosing/outer function aka BAG THEORY
# here is result f2 is stored so we are basically calling f2



def chaicoder(num):
    def actual(y):
        return y ** num
    return actual

f = chaicoder(2)
print(f)
g = chaicoder(3)

print(f(3))
print(g(3))



