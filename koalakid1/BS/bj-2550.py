from bisect import bisect_left
import sys

input = sys.stdin.readline

def lis(line):
    global n
    dp = [0 for i in range(n)]
    fr = [0 for i in range(n+1)]
    size = 0
    for i in range(n):
        h = bisect_left(dp[:size],line[i])
        if h == size:
            size += 1
        dp[h] = line[i]
        fr[dp[h]] = dp[h-1] if h else 0
    i = dp[size-1]
    lis_list = []
    while i:
        lis_list.insert(0,i-1)
        i = fr[i]
    return lis_list




if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().strip().split()))
    b = list(map(int,input().strip().split()))
    b_index = [b.index(a[i])+1 for i in range(n)]
    
    l = lis(b_index)
    print(len(l))
    result = sorted([b[i] for i in l])
    for i in result:
        print(i, end=" ")
