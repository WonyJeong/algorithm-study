#1546

import sys
input = sys.stdin.readline
N = int(input())
score = list(map(int,input().strip().split()))
max = 0
sum = 0
for i in score :
    sum += i
    if i>max :
        max = i
print((sum/max)*100/N)