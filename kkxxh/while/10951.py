#10951
import sys

input = sys.stdin.readline
A,B = map(int, input().strip().split())
while(1) :
    try :
        print(A+B)
        A,B = map(int, input().strip().split())
    except :
        break

#try-except처리 안할 경우 런타임에러 발생