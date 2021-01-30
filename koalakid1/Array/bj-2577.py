import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

abc = str(a * b * c)
list = [0 for _ in range(10)]

for i in abc:
    list[int(i)] += 1

for i in list:
    print(i)
