# Tuples are same as lists but they are immutable
tea_types = ("Black", "Green", "Oolong")
print(tea_types)

print(tea_types[0])
print(tea_types[-1])
print(tea_types[1:])

print(len(tea_types))

# CONCATANATION
more_tea = ("Earl Grey", "Herbal", "Black")
all_tea = more_tea + tea_types
print(all_tea)

if "Green" in tea_types:
    print("I have green tea")

print(all_tea.count("Black"))