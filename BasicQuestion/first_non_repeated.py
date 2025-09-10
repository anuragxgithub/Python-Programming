str = "anuragunbn"
flag = 0

for ch in str:
    if str.count(ch) == 1:
        print("First non repeated character in string is : ", ch)
        flag += 1
        break

if flag == 0:
    print("There is no non repeated character in the string")

