import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    string = input().strip()
    result = 0
    for i in string:
        if i == "(":
            result += 1
        else:
            result -= 1
        if result < 0:
            break
    if result == 0:
        print("YES")
    else:
        print("NO")
