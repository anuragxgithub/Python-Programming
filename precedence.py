print(1 == 2 < 3)
print(1 == 1 < 3)

'''
Python's chained comparisons automatically insert and operators between each comparison pair, and each value is only evaluated once. So a == b < c becomes (a == b) and (b < c), not (a == b) < c.
You can verify this by running:
'''
