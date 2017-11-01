while True:
    try:
        students = int(input("Enter int number of students\n"))
        if students >= 0:
            break
    except ValueError:
        print ("\nWhat you entered is not a number")
while True:
    try:
        apples = int(input("Enter int number of apples\n"))
        if apples >= 0:
            break
    except ValueError:
        print ("\nWhat you entered is not a number")

print(apples//students," apples got each student and ", apples % students," left in the basket")
