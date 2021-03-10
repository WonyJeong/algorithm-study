import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    d = [[0 for _ in range(10)] for _ in range(n)]
    d[0][1:] = [1 for _ in range(9)]
    
    for i in range(1,n):
        for j in range(10):
            if j == 0:
                d[i][j] = d[i-1][j+1]
            elif j == 9:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = d[i-1][j-1] + d[i-1][j+1]
    print(sum(d[n-1])%1000000000)