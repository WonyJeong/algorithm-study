#2562
import sys

input = sys.stdin.readline
Arr = list()
max = 0

for i in range(9) : 
    a = int(input().strip())
    Arr.append(a)
    
    if(max < Arr[i]) :
        max = Arr[i]


print(max)
print(Arr.index(max)+1)
