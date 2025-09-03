print(0.1 + 0.1 + 0.1) # but the o/p is 0.30000000000000004
# floating-point representation limitations
print(1.2 + 3.2 + 4.5)

print(0.1 + 0.1 + 0.1 == 0.3)
# Output: False
print(0.2 + 3.2)

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))
'''
Binary representation problem: Computers store floating-point numbers in binary (base-2), but 0.1 cannot be represented exactly in binary, just like 1/3 cannot be represented exactly in decimal (0.333...).
IEEE 754 standard: Python uses double-precision floating-point numbers, which have limited precision. The closest binary approximation to 0.1 is slightly larger than the true value.
'''