while True:
    try:
        k1 = float(input())
        if k1 >= 0:
            break
    except ValueError:
        print ("\nWhat you entered is not a number")
while True:
    try:
        k2 = float(input())
        if k2>= 0:
            break
    except ValueError:
        print ("\nWhat you entered is not a number")
        
print("square is ", k1*k2/2)
