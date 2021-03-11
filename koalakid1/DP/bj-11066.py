import sys
from bisect import bisect_left

if __name__ == "__main__":
    input = sys.stdin.readline
    for _ in range(int(input())):
        n = int(input())
        l = list(map(int,input().strip().split()))
        dp = [[] for _ in range(n)]


import sys 
input = sys.stdin.readline 
t = int(input()) 
for __ in range(t): 
    k = int(input())
    page = list(map(int, input().split())) 
    table = [[0]*k for _ in range(k) ] 
    for i in range(k-1): 
        table[i][i+1] = page[i] + page[i+1] 
        for j in range(i+2, k): 
            table[i][j] = table[i][j-1] + page[j] 
    for d in range(2, k): 
        for i in range(k-d): 
            j = i+d 
            minimum = [table[i][k] + table[k+1][j] for k in range(i, j)] 
            table[i][j] += min(minimum) 
    
    print(table[0][k-1])
