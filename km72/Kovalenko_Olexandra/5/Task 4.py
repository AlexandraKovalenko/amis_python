count = input("Введите пару N:K: ").split()
N = int(count[0])
K = int(count[1])
i = 0
li = []
ri = []
line = [x for x in "I"*N]
while i < K:
    li_ri = input("Введите пару li:ri: ").split()
    li.append(int(li_ri[0]))
    ri.append(int(li_ri[1]))
    i += 1
for b in range(K+1):
    for i in (li[b], ri[b]+1):
        line[i] = "."
print(line)
