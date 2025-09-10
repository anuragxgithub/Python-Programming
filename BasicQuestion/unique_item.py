items = ["apple", "banana", "orange", "apple", "mango"]

# M-1
for i in items:
    if(items.count(i) > 1):
        print("Duplicate item is : ", i)
        break

# M-2
unique_items = set()
for i in items:
    if(i in unique_items):
        print("Duplicate item is : ", i)
        break
    else:
        unique_items.add(i)
    
