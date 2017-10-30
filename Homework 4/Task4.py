print("Введіть рік")
while True:
    try:
        year=int(input())
        if year >= 0:
            break
    except:
        print("Please enter number")

if year%4==0:
    print("LEAP")
else:
    print("COMMON")
            
