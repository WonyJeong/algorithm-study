#3052
import sys
input = sys.stdin.readline
num = [0,0,0,0,0,0,0,0,0,0]
differ = 0
for i in range(0,10) :
    num[i] = int(input().strip())%42
print(len(set(num)))
