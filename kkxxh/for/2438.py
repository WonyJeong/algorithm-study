#2438
import sys

input = sys.stdin.readline
N= int(input())
for i in range(N) :
    for j in range(i+1) :
        print("*",end="")
    print("")