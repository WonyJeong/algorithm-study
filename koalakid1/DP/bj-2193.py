import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())

    d1 = [0 for _ in range(n+1)]
    d2 = [0 for _ in range(n+1)]

    d1[1] = 1
    for i in range(2,n+1):
        d1[i] = d2[i-1]
        d2[i] = d1[i-1] + d2[i-1]
    print(d1[n]+d2[n])