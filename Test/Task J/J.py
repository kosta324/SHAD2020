with open("input.txt", "r") as f:
    n = int(f.readline())
    a = []
    line = f.readline()
    for x in line.split(' '):
        a.append(float(x))
    q = int(f.readline())
    with open("output.txt", "w") as file:
        for line in f:
            r, l = line.split(' ')
            r = int(r)
            l = int(l)
            col = l - r + 1
            res = 0
            for j in range(col):
                res += a[j + r]
            res = res/(col)
            file.write(("%.6f\n" % (res)))