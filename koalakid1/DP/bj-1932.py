import sys
from bisect import bisect_left

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    d = [[] for i in range(n)]
    for i in range(n):
        if i == 0:
            d[i].append(int(input()))
        else:
            l = list(map(int,input().strip().split()))
            for j in range(len(d[i-1])):
                if i == 1:
                    d[i].append(d[i-1][j] + l[j])
                    d[i].append(d[i-1][j] + l[j+1])
                else:
                    print(len(d[i-1]))
                    if j == 0:
                        d[i].append(d[i-1][j] + l[j])
                        d[i].append(max(d[i-1][j],d[i-1][j+1]) + l[j+1])
                    elif j == len(d[i-1])-1:
                        d[i].append(d[i-1][j] + l[j+1])
                    else:
                        d[i].append(max(d[i-1][j],d[i-1][j+1]) + l[j+1])
                print(l,d)
    print(max(d[n-1]))