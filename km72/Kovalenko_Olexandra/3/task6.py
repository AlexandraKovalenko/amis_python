sumOfDesks = 0

for i in range(3):
    while True:
        try:
            N = int(input("Enter int number of students of group " + str(i+1) + "\n"))
            if N >= 0:
                break
        except ValueError:
            print ("\nEnter correct value")
    sumOfDesks += N // 2 + N % 2
  
print("They need to buy ",sumOfDesks," desks")
