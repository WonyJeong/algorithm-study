#8393
import sys
input = sys.stdin.readline
N = int(input().strip())
sum = 0
for i in range(1,N+1) :
    sum += i
print(sum)