print("Введіть х")
while  True:
    try:
        x = float(input())
        break
    except:
        print("Please enter number")
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)
