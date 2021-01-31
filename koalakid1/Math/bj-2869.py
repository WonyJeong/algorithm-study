import sys
import math

input = sys.stdin.readline

A, B, V = map(int, input().strip().split())

VA = V-A
AB = A-B
day = 1
otherDay = math.ceil(VA/AB)
if otherDay < 0:
    otherDay = 0

print(day + otherDay)
