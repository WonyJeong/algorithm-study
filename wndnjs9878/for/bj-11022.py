#11022
import sys
input = sys.stdin.readline
T = int(input().strip())
for i in range(1,T+1):
    A, B = map(int, input().strip().split())
    print("Case #%d:"%i, A,"+", B, "=", A+B)