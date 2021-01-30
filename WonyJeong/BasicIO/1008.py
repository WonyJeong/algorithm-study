import sys
input = sys.stdin.readline

A, B = map(float, input().strip().split())

print(A* (10**9) / B)
print(  (A* (10**9) / B) / 10**9  ) 