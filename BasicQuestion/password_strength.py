password = input("Enter your password: ")
len = len(password)

if(len < 6):
    print('Weak')
elif(len < 10):
    print("Medium")
else:
    print("Strong")