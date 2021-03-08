import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    k = [int(input()) for _ in range(n)]

    if n == 1 or n == 2:
        print(sum(k))
    else:
        d = [0 for _ in range(n)]
        d[0] = k[0]
        d[1] = k[0] + k[1]
        for i in range(2,n):
            d[i] = max(d[i-3] + k[i-1] + k[i], d[i-2] + k[i])
        print(d[n-1])