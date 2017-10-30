while True:
    try:
        x1=int(input())
        break
    except:
        print("Please enter number")
while True:
    try:
        y1=int(input())
        break
    except:
        print("Please enter number")
while True:
    try:
        x2=int(input())
        break
    except:
        print("Please enter number")
while True:
    try:
        y2=int(input())
        break
    except:
        print("Please enter number")
if (x1+x2)%2==0 and (y1+y2)%2==0:
    print("YES")
elif (x1+x2)%2!=0 and (y1+y2)%2!=0:
    print("YES")
else:
    print("NO")
