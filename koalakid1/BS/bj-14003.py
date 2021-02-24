from collections import deque
from bisect import bisect_left
import sys

input = sys.stdin.readline

def lis(line):
    global n
    dp = [0 for i in range(n)]
    fr = [0 for i in range(n)]
    size = 0
    for i in range(n):
        fr[i] = bisect_left(dp[:size], line[i])
        if fr[i] == size:
            size += 1
        dp[fr[i]] = line[i]
    print(size)
    lis_list = []
    size -= 1
    for i in range(n-1,-1,-1):
        if fr[i] == size:
            lis_list.insert(0,line[i])
            size -= 1
    print(*lis_list)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().strip().split()))
    
    lis(a)