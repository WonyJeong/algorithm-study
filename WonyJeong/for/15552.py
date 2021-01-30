import sys
input = sys.stdin.readline

N = int(input().strip())

for i in range(0,N):
    a, b = map(int , input().strip().split())
    print(a+b)