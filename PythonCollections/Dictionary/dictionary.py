# Dictionaries are mutable data types in python.
# it consists of key value pair and keys should be unique
# if you add keys which is already present its value gets overridden
dict = {"Name": "Anurag", "Class": "10", "Location": "Bhopal"}
print(dict)
print(len(dict))

# ACCESSING KEYS AND VALUES
print(dict["Location"])  # if key not found then give ERROR
print(dict.get("Luli"))  # if key not foudn then return NONE

for info in dict:  # 'info' will give keys
    print(info, "-", dict[info])

for key, value in dict.items():  # accesing both key and value
    print(key, value, end=" || ")

# UPDATING VALUES
print()
dict["Name"] = "Rahul"
print(dict)

# ADDING ITEMS
dict["new key"] = "new value"
print(dict)

# REMOVING/DELETING ITEMS
dict.pop("Class")   # removes the item of specified key and returns its value
print(dict)
dict.popitem()    # this simply deletes and return the last item of the dict
print(dict)
# dict.clear()      # empties the dictionary

del dict["Location"]
'''
"del" effectively removes references to objects, and if no other references to that object exist, the object itself may be garbage-collected, freeing up memory.
used to delete objects, elements from collections, or even entire variables
'''
print(dict)



dict_copy = dict.copy()   # new copy of dictionary will be created and reference to it will be given to dict_copy


# 2D DICTIONARY
city_info = {"city1": {"Name" : "Bhopal", "State": "MP"},
             "city2": {"Name" : "Lucknow", "State": "UP"}
             }

print(city_info)
print(city_info["city1"])
print(city_info["city1"]["State"])

# DICTIONARY COMPREHENSION
squared_num = {x:x**2 for x in range(6)}
print(squared_num)

 
# CONSTRUCTING DICTIONARY FROM GIVEN KEYS IN LIST ⚠️
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)