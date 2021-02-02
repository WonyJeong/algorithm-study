#10871
import sys

input = sys.stdin.readline
N, X = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
for i in range(N):
    if (A[i] < X ) : print(A[i], end=" ")