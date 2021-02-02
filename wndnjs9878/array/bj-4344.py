#4344
import sys
input = sys.stdin.readline
C = int(input())
for i in range(0,C) :
    N = list(map(int, input().split())) #N[0] : numberOfStudents
    avg = sum(N[1:])/N[0]
    cnt = 0
    for score in N[1:]:
        if score > avg :
            cnt += 1
    print(str('%.3f' % round(cnt/N[0]*100, 3)) + '%')
    