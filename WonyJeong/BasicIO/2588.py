import sys
input = sys.stdin.readline

A =  int(input().strip())
B =  input().strip()

print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))