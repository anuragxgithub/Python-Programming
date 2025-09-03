l1 = [1,2,3]
l2 = l1

print(l1)
print(l2)

l1 = "Anurag"
l1 = [1,2,3]    # here reference changes
print(l1)
print(l2)
print(l1 is l2)

l1[0] = 44
print(l1)
print(l2)


