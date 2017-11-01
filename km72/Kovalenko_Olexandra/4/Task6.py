print("Щоб визначити, чи може фігура перейти з однієї клітинки в іншу за один крок, введіть координати точок.")
print("Please print x1")
while True:
    try:
        x1=int(input())
        break
    except:
        print("Please enter number")
print("Please print y1")
while True:
    try:
        y1=int(input())
        break
    except:
        print("Please enter number")
print("Please print x2")
while True:
    try:
        x2=int(input())
        break
    except:
        print("Please enter number")
print("Please print y2")
while True:
    try:
        y2=int(input())
        break
    except:
        print("Please enter number")

if x1==x2 or y1==y2:
    print("Yes")
else:
    print("No")
        
        
        
