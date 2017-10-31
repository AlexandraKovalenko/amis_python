list = {}
num = int(input("Enter a number of students\n"))
height = int(input("enter a height of Petya\n"))
i = 0
petyaPosition = 0
print("Enter a non-descending sequence")
while i < num:
    list[i] = input("Enter an height of student\n")
    print(i)
    if list[i].isdigit():
        if int(list[i]) > 0 & int(list[i]) <= 200:
            list[i] = int(list[i])
            if height <= list[i]:
                petyaPosition = i + 1
            i += 1
answer = "position ", petyaPosition  + 1 
print(answer) 
