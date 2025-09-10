names = ["Anurag", "Rahul", "Rohit", "Shivam"]
print(names)

# ACCESSING ELEMENTS
print(names[0])
print(names[-1])

# SLICING
print(names[0:3])
print(names[:3])
print(names[2:])

# UPDATING
names[0] = "Dhriti"
print(names)

# ⚠️
names[1:2] = "anurag"
'''
Here you are assigning to a slice, which means Python expects an iterable of elements.
"anurag" is a string, and since strings are iterable, it is treated like:
['a', 'n', 'u', 'r', 'a', 'g']
So the slice [1:2] (which was ["Rahul"]) is replaced with all six characters.
'''
print(names)
print(type(names[1]))
# to fix this:
names = ["Dhriti", "Rahul", "Rohit", "Shivam"]
# names[1:2] = ["anurag", "kruskal"]
names[1:3] =["anurag", "kruskal"]
print(names)

names = ["Anurag", "Shivam", "Aryan", "Dhritiman"]
print(names)

print(names[1:1])  # prints empty list

names[1:1] = ["Kartik"]  # but here will update the idx 1 element
print(names)

# REMOVING ELEMENTS
names = ["Anurag", "Shivam", "Aryan", "Dhritiman"]
# names.remove("Aryan")     # removes first occurence of given element
# names.pop()               # return and remove the last item of list
# ⚠️ removing multiple itmes at once
names[1:3] = []    # assigning empty list meaning removing that item
print(names)


# ADDING ELEMENTS TO LIST
names = ["Anurag", "Shivam", "Aryan", "Dhritiman"]
names.append("kalia")        # add item at the end of list
names.insert(0, "Mustang")   # insert item at specified indx
print(names)
another_list = ["Nigga"]
# another_list = "Nigga"
names.extend(another_list) # extend() keyword adds multiple elements from an iterable(list, tuple, string, ..)
print(names)

# l2 = ["shruti", "jiya"]
# new_list = names + l2;     # list concatenation
# print(new_list)



# ITERATING IN LIST
tea = ["black", "ginger", "green", "masala"]
for t in tea:
    # print(t)       # by default each item is printed in new line
    print(t, end="-") # you can change to this

if "green" in tea:
    print("I have green tea.")






# REFERENCE STUFF IN ASSIGNING VAR TO LIST
list1 = [1,2,3,4]
list2 = list1      # here list2 is pointing to the same memory reference where list1 is pointing

list3 = list1.copy() # but here new copy of list1 is created and now list3 is pointing to it
list1.append(5)
print(list1, list3)   # proof

# List Comprehension (for adding items based on a condition or transformation):
list_compr = [x for x in range(11)]
print(list_compr)
squared_num = [x**2 for x in range(6)]
print(squared_num)
odd_nums = [x for x in range(1, 11, 2)]
print(odd_nums)
