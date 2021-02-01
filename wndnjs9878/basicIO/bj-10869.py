#10869
import sys
input = sys.stdin.readline
A, B = map(int, input().strip().split())
print(A+B, A-B, A*B, int(A/B), A%B, sep='\n')