#2562
import sys
input = sys.stdin.readline
max = 0
index = 0
for i in range(0, 9) :
    num = int(input())
    if max < num : 
        max = num
        index = i+1

print(max, index, sep='\n')