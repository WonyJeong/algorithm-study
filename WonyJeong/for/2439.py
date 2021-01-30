import sys
input = sys.stdin.readline

N = int(input().strip())

for i in range(0,N):
    for j in range(0,N):
        dot = "*" if i+j >= N-1 else " "
        print(f'{dot}', end = "") 
    print("")