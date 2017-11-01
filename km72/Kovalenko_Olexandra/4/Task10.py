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
if x1==y1 or x2==y2:
    print("YES")
elif (x1/y1)==(x2/y2):
    print("YES")
elif  (x1+x2)==(y1+y2)  or (x1-x2)==(y1-y2):
    print("YES")   
else:
    print("NO")
