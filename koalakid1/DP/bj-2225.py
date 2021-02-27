import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n, k = map(int, input().split())
    s = [[0] * (n+1) for _ in range(k+1)]
    s[0][0] = 1
    for i in range(1, k+1):
        for j in range(n+1):
            s[i][j] = s[i-1][j] + s[i][j-1]
    print(s[k][n] % 1000000000)
