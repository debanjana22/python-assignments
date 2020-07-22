num = int(input('Please enter a number: '))
flag = 0
for each in range(2, num):
    remainder = num % each
    if remainder == 0:
        flag = 1
        break

if flag == 1:
    print (f"{num} is not a prime number")
else:
    print (f"{num} is a prime number")