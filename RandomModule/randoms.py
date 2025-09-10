import random

print(random.random())  # prints any real num b/w 0 and 1

# but python can also select random integers from any given range
print(random.randint(1,101))

l1 = ['lemon tea', 'mint tea', 'masala chai', 'ginger tea']
print(random.choice(l1))
random.shuffle(l1)
print(l1)

# Generate a random float between a and b (inclusive of a, exclusive of b)
# The range can be any two numbers, including decimals.
print(random.uniform(2.2, 6.5))