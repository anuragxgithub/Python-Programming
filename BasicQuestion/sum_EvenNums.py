n = int(input("Enter the number till which you want sum of even nums: "))
list = []
sum = 0
for i in range(2, n+1, 2):
    list.append(i)
    sum += i

print(list)
print("Sum is : ", sum)