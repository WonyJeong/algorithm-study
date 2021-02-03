#8958
import sys

input = sys.stdin.readline
N= int(input().strip())
for i in range(N):
    score = 0
    sum =0
    answer = input().strip()
    for j in range(len(answer)) :
        if answer[j] == 'X' :
            score = 0
        else :
            score += 1
            sum += score
    print(sum)