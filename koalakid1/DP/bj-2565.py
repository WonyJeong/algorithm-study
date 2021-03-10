import sys
from bisect import bisect_left

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    A = []
    B = []
    AB = []
    for _ in range(n):
        AB.append(list(map(int,input().strip().split())))
    
    AB = sorted(AB, key = lambda x:x[0])
    
    for i,j in AB:
        A.append(i)
        B.append(j)
    
    lis = [B[0]]
    for i in range(1,n):
        if lis[-1] < B[i]:
            lis.append(B[i])

        elif lis[-1] > B[i]:
            lis[bisect_left(lis,B[i])] = B[i]
            
    print(n - len(lis))