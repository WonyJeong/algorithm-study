#8393
import sys

input = sys.stdin.readline
n = int(input().strip())
sum = 0
for i in range(n+1) :
    sum += i
print(sum)
    