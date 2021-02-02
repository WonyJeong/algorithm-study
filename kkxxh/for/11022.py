#11022
import sys

input = sys.stdin.readline
N = int(input())
for i in range(N):
    a,b = map(int, input().strip().split())
    print("Case #%d:"%(i+1),a,"+",b,"=",a+b)