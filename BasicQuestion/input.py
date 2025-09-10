'''

input = int(input("Enter the number: "))
 
while not(input > 1 and input < 10):
    input = int(input("Re-enter the number: "))  # why this is wrong? because: this time input is referring to our variable not the fn

print("Entered number is : ", input)

'''

# num = int(input("Enter a number b/w 1 and 10: "))
 
# while not(num > 1 and num < 10):
#     num = int(input("Invalid number try again: "))  # why this is wrong? because: this time input is referring to our variable not the fn

# print("Entered number is : ", num)


# M-2
while True:
    num = int(input("Enter a number b/w 1 and 10: "))
    if  1 < num < 10:
        print("Your entered number is : ", num)
        break
    else:
        print("Invalid number try again: ")
    