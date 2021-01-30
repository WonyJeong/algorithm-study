import sys

input = sys.stdin.readline
num = input().strip()
result = [int(num)]

while True:
    add = 0
    for i in str(result[-1]):
        add += int(i)
    num = int(str(add)[-1]) + int(str(result[-1])[-1]) * 10
    if num == result[0]:
        break
    result.append(num)

print(len(result))
