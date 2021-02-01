#10950
import sys
input = sys.stdin.readline
T = int(input().strip())
for i in range(0,T) :
    A, B = map(int, input().strip().split())
    print(A+B)