#4344
import sys

input = sys.stdin.readline
N = int(input().strip())
for i in range(0,N):
    sum=0
    aver= 0
    count=0
    score = list(map(int,input().strip().split()))
    for j in range(1,len(score)) :
        sum += score[j]
    aver = sum / score[0]
    for j in range(1,len(score)):
        if score[j] > aver : 
            count += 1
    print("%.3f%%" %round((count/score[0])*100,3))  