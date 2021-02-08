#2292
import sys

input = sys.stdin.readline
N = int(input().strip())
step = 0
i = 1
while(1) :
    i += 6 * step
    if N <= i : break
    step += 1
print(step+1)