#2739
import sys

input = sys.stdin.readline
a = int(input().strip())
for i in range(1,10):
    print(a, "*", i ,"=", a*i)
