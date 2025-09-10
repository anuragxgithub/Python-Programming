age = int(input("Enter your age : "))
day = input("Enter day: ")

if age < 18:
    if day=="wednesday" or day=="Wednesday":
        print("Ticket price: $6")
    else:
        print("Ticket price: $8")
    
else:
    if day=="wednesday" or day=="Wednesday":
        print("Ticket price: $10")
    else:
        print("Ticket price: $12")

# M-2

price = 8 if age <18 else 12
if day=="wednesday" or day=="Wednesday":
    print("Ticket price is : $", price-2)
else:
    print("Ticket price is : $", price)