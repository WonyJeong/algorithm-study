#15552
import sys

input = sys.stdin.readline
N = int(input())
for i in range(N) :
    a,b = map(int, input().strip().split())
    print(a+b)