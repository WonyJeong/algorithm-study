import sys

input = sys.stdin.readline

num = input().strip()
number = input().strip()

result = 0
for i in number:
    result += int(i)

print(result)
