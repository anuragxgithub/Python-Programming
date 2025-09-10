str = "0123456789"
name = "Anurag"
full_name = "   Anurag Jaiswal  "

# All these operations on str does not changes actual string bcz strings are immutable

# SLICING
print(str[:])
print(str[3:])
print(str[3:6])
print(str[0:8:2])
print(str[0:8:3])

# UPPER/LOWER CASE
print(name.lower())
print(name.upper())

# REMOVING SPACES
print(full_name.strip())  # note it only removes traling or leading spaces not (in b/w)

# SPLITTING INTO A LIST
chai = "Lemon, Ginger, Mint, Masala"
print(chai.split())  # when there is not arg. present it splits the string at spaces & store in a list
print(chai.split(", "))  # split when comma with space is encountered

# FIND THE INDEX OF CHAR OR ANY STRING  (return -1 on failure)
chai = "Masala Chai"
print(chai.find("Chai"))
print(chai.find('a'))

chai = "masala chai chai chai chai"
print(chai.count("chai"))

# PLACEHOLDERS AND FSTRING ⚠️
chai = "Masala Chai"
quantity = 2
message = "I ordered {} cups of {}!!"
print(message.format(quantity, chai))

name = "Anurag"
age = 21
msg = f"Hi, I am {name} and I am {age} years old."   # formatted string
print(msg)

# LIST TO STRING
l1 = ["Lemon", "Ginger", "Mint", "Masala"]
print("".join(l1))
print(" ".join(l1))
print("-".join(l1))


# LENGTH
print(len(l1))

# SYMBOLS INSIDE STRING

# msg = "He said, "Masala Chai is awesome!""   # see giving error  double quotation inside string
msg = "He said, \"Masala Chai is awesome!\"" 
print(msg)
#using back slashes
msg = "Anurag Jaiswal\n21"  # i want to print it as it is
print(msg)  # but printed in different line
print(r"Anurag Jaiswal\n21")   # USING RAW STRING

# CHECKING ELEMENT PRESENT OR NOT 
str = "Anruag Jaiswal Khalilabad and Bhopal"
print("Bhopal" in str)