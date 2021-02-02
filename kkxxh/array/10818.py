#10818
import sys

input = sys.stdin.readline
N = int(input().strip()) 
Arr = list(map(int, input().strip().split()))

max = -1000000
min = 1000000

for i in range(N):
    if Arr[i] > max :
        max = Arr[i]
    if Arr[i] < min :
        min = Arr[i]

print(min, max)