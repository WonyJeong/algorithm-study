import sys

input = sys.stdin.readline


data = {(a, b, c): 0 for a in range(21) for b in range(21) for c in range(21)}

data[(0, 0, 0)] = 1


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return data[(0, 0, 0)]
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if data[(a, b, c)] != 0:
        return data[(a, b, c)]

    if a < b and b < c:
        data[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        data[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + \
            w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return data[(a, b, c)]


while True:
    a, b, c = map(int, input().strip().split())
    if a == b == c == -1:
        break
    print(f"w\({a}, {b}, {c}\) = {w(a, b, c)}")
