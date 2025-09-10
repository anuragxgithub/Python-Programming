str = input("Enter a string: ")

len = len(str)
temp = ""
for i in range(len):
    temp += str[len-(i+1)]

print(temp)

# M-2

reversed_str = ""
for ch in str:
    reversed_str = ch + reversed_str
print(reversed_str)



# for i in range(-5, -1):
#     print(i)

# NOTE: in range function range(i,j)  i should be smaller than j