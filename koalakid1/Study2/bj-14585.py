import sys
import math
input = sys.stdin.readline
        

if __name__ == "__main__":
    n,m = map(int,input().strip().split())
    graph = [[0 for _ in range(302)] for _ in range(302)]
    dp = [[0 for _ in range(302)] for _ in range(302)]
    for i in range(n):
        x,y = map(int,input().strip().split())
        graph[x+1][y+1] = m - y - x if m >= y + x else 0
    
    for i in range(1,302):
        for j in range(1,302):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + graph[i][j]
    print(dp[301][301])