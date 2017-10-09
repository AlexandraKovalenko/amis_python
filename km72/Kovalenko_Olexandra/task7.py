while True:
    try:
        N = int(input("Enter int number of minutes\n"))
        if N >= 0:
            break
    except ValueError:
        print ("\nWhat you entered is not a number")
  
print((N % 1440) // 60, ":", (N % 1440) % 60)
