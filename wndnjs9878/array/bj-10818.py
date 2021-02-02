#10818
import sys
input = sys.stdin.readline
N = int(input().strip())
array = list(map(int,input().strip().split()))
max = array[0]
min = array[0]
for i in range(0, N) :
    if max < array[i] : max = array[i]
    if min > array[i] : min = array[i]
print(min, max)