i = 0
x =[]
y = []
a = 'NO'
while i < 8:
    x_y = input("Введите пару x:y: ").split()
    x.append(int(x_y[0]))
    y.append(int(x_y[1]))
    i += 1
for pos1 in range(0, 8):
    for pos2 in range(0, 8):
        if pos1 == pos2:
            continue
        if abs(x[pos1] - x[pos2]) == abs(y[pos1] - y[pos2]) or (x[pos2] == x[pos1] or y[pos2] == y[pos1]):
            a = 'YES'
            break
print(a)
