num = int(input("Enter a number of elements of the list"))
print("Enter a list of numbers")
list = {}
i = 0
while i < num:
    list[i] = input("Enter a number\n")
    if list[i].isdigit():
        list[i] = int(list[i])
        i += 1

flag = 1
start = 0
i = start

while start < num:
    i = 0
    flag = 1
    while i < num:
        if (i != start) & (list[start] == list[i]):
            flag = 0
            
            break
        i +=1
    if flag:
        print(list[start])
    
    start += 1

