print("Введіть перше число")
while True:
    try:
        x1=int(input())
        break
    except:
        print("Please enter number")
print("Введіть друге число")     
while True:
    try:
        y1=int(input())
        break
    except:
        print("Please enter number")
print("Введіть третє число")     
while True:
    try:
        x2=int(input())
        break
    except:
        print("Please enter number")
print("Введіть четверте число")
while True:
    try:
        y2=int(input())
        break
    except:
        print("Please enter number")
if abs(x1-y1)==2 and abs(x2-y2)==1:
    print("YES")
elif abs(x1-y1)==1 and abs(x2-y2)==2:
    print("YES")
else:
    print("NO")
