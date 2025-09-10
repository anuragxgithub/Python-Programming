# n = 4
# if(n == 1 or n == 2 or n == 3):
#     print("Number is prime")
#     exit()
# for i in range(2, int(n/2)+1):
#     if n % i == 0:
#         print("The number is not prime.")
#         break
#     if i == int(n/2):
#         print("The number is prime.")


n = 4
isPrime = True

for i in range (2, int(n/2)+1):
    if n % i == 0:
        isPrime = False
        break

if isPrime: print("Number is prime") 
else: print("Number is not prime")