#2869
import sys
import math

input = sys.stdin.readline
A, B, V = map(int, input().strip().split())
print(math.ceil((V-A)/(A-B)) + 1)

#math 