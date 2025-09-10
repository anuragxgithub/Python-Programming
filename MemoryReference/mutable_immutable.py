# For understanding references in memory (variable to value)
x = 10
y = x

print(x)
print(y)

x = 20
print(x)
print(y)

str = "Anurag"
print(str)
str = "Rahul"
print(str)  
# but strings are immutable so why it got changed??
# actually string itself is not changing only the reference of variable is changing