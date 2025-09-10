'''
🔹 yield in Python

The yield keyword is used in a function to make it a generator.
Instead of returning a value once (like return), a generator 
can pause execution, "remember" its state, and resume later.

🔑 Key points about yield:
1. yield is like return, but it doesn’t end the function permanently.
2. Each time the generator function is called (via next() or a loop), execution continues from where it left off.
3. It’s very memory-efficient for large data (since it generates values one at a time instead of storing all of them).
'''


def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))

print("------------------------")

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

print(count_up_to(5))
'''
count_up_to(5) does not return a list.
It returns a generator object.
When you print it directly, Python will just display something like:
<generator object count_up_to at 0x0000021B67AE3430>
That memory address is just Python telling you:
👉 “This is a generator, not the actual values.”
You need to iterate over the generator to get its values:
1. convert it into list  print(list(count_up_to(5)))
2. Use a loop (like here we did):
3. Manual next() calls:

'''
for num in count_up_to(5):
    print(num)




# QUESTION: Write a generator function that yields even numbers up to a specified limit
def even_nums(n):
    for i in range(0, n+1, 2):
        yield i

print(list(even_nums(10)))
for i in even_nums(10):
    print(i)


'''
A function becomes a generator function if it contains at least one yield statement.
When you call such a function, it doesn’t run immediately like a normal function.
Instead, it returns a generator object (which is an iterator).
'''