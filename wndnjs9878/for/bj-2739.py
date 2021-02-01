#2739
import sys
input = sys.stdin.readline
N = int(input().strip())
for i in range(1,10) :
    print(N, "*", i, "=",  N*i)