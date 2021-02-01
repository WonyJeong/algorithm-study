#2438
import sys
input = sys.stdin.readline
N = int(input().strip())
for i in range(0, N) :
    for m in range(0,i+1):
        print("*", end='')
    print()
    