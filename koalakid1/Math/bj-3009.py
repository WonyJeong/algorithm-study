import sys

input = sys.stdin.readline

x = {}
y = {}
other_x = []
other_y = []
for i in range(3):
    _x, _y = map(int, input().strip().split())
    if _x not in x:
        x[_x] = [i]
        other_x.append(_x)
    else:
        other_x.remove(_x)
    if _y not in y:
        y[_y] = [i]
        other_y.append(_y)
    else:
        y[_y].append(i)
        other_y.remove(_y)

print(f"{other_x[0]} {other_y[0]}")
