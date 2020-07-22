sum = 0;
while True:
    num = eval(input("Please enter a number (To cancel press 0): "))
    sum += num
    if num == 0:
        break

print(f"Sum of the numbers entered by you is: {sum}")