#10952
import sys
input = sys.stdin.readline
A, B = map(int, input().strip().split())
while A != 0 and B != 0 :
    print(A+B)
    A, B = map(int, input().strip().split())