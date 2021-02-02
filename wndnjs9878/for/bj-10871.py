#10871
import sys
input = sys.stdin.readline
N, x = map(int, input().strip().split())
A = list(map(int,input().strip().split()))
for i in range(0,N):
    if int(A[i]) < x : print(A[i], end=' ')