#2588
import sys
input = sys.stdin.readline
A = int(input().strip())
B = input().strip()
print(A*int(B[2]), A*int(B[1]), A*int(B[0]), A*int(B), sep='\n')