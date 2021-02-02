#2577
import sys
input = sys.stdin.readline
multiplied = 1
for i in range(0,3) :
    multiplied *= int(input())
result = str(multiplied)
array = [0,0,0,0,0,0,0,0,0,0]
for i in range(0,len(result)) :
    array[int(result[i])] += 1

for _ in array :
    print(_)
