import sys
from bisect import bisect_left
input = sys.stdin.readline
        

if __name__ == "__main__":
    n,k = map(int,input().strip().split())
    x = sorted([int(input()) for _ in range(n)])
    
    a = bisect_left(x,x[0]+k)
    result = k + sum(x[:a])
    
    print(result // a)