print("Enter 3 numbers to get their sum")

sum = 0

for i in range(3):
    while True:
        try:
            sum += float(input())
            break
        except ValueError:
            print ("\nWhat you entered is not a number")

print("sum is ", sum)
