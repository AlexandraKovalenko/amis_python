while True:
    try:
        N = int(input("Enter int number\n"))
        if N >= 0:
            break
    except ValueError:
        print ("\nWhat you entered is not a number")
  
print("The next number for the number {0} is {1}.\nThe previous  number for number {0} is {2}.".format(N, N+1, N-1))
