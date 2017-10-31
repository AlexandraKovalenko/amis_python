print("Введіть перше число")
while True:
    try:
        x=int(input())
        break
    except:
        print("Please enter number")
print("Введіть друге число")     
while True:
    try:
        y=int(input())
        break
    except:
        print("Please enter number")
print("Введіть третє число")     
while True:
    try:
        z=int(input())
        break
    except:
        print("Please enter number")
print("Введіть четверте число")
if x*y-z==x or x*y-z==y and x*y>z and z!=1:
    print('YES')
elif (x*y-z)%2==0 and x*y>z and z!=1:
    print('YES')
else:
    print('NO')
