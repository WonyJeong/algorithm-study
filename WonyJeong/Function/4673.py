def dn(num):
    _num = num
    result = _num
    while True:
        if _num == 0:
            break

        result += int(_num % 10)
        _num = _num // 10

    return result


arr = []
for _ in range(0, 10101):
    arr.append(False)

idx = 1
while True:
    nonSelfNumber = dn(idx)

    if nonSelfNumber > 10100:
        break

    arr[nonSelfNumber] = True
    idx += 1

for i in range(1, 10001):
    if arr[i] == False:
        print(i)
