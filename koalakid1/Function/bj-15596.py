def selfNum(a):
    b = 0
    for i in str(a):
        b += int(i)
    b += a
    return b


a = set()
b = set()
for i in range(1, 10001):
    b.add(i)
    a.add(selfNum(i))
for i in sorted(b-a):
    print(i)
