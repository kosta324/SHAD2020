with open("input.txt", "r") as f:
    n = int(f.readline())
    a = []
    line = f.readline()
    for x in line.split(' '):
        a.append(int(x))
i = 0
while i < n:
    x = a[i]
    k = a.count(x)
    if k > 1:
        for j in range(k-1):
            a.remove(x)
            n -=1
    else:
        i += 1
with open("output.txt", "w") as file:
    file.write('%i\n' % (i))
    for j in range(i):
        file.write('%i ' % (a[j]))