import sys
input = sys.stdin.readline

N = int(input().strip())

for i in range(1,N+1):
    for j in range(0,i):
        print("*" ,end="")
    print("")