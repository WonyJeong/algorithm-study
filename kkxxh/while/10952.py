#10952
import sys

input = sys.stdin.readline
A,B = map(int, input().strip().split())
while (A != 0 and B != 0) :
    print(A+B)
    A,B = map(int, input().strip().split())


# while(1):
#     a,b=map(int,input().split())
#     if(a==0 and b==0):
#          break
#     else :
#          print(a+b)