print("Яке з введених чисел є найменшим ")
print("Число 1")
while True :
    try:
        n1=int(input())
        break
    except:
        print("Please enter number")
print("Число 2")
while True :
    try:
        n2=int(input())
        break
    except:
        print("Please enter number")

minimum = n1

if n2< minimum:
          minimum = n2

print("minimum")
