from collections import deque
import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    d = [1 for _ in range(n+1)]
    d[1] = 2
    s = 0
    for i in range(2, n+1):
        d[i] = (d[i-1] * 2 + d[i-2] * 3 + 2 * s) % 1000000007
        s += d[i-2]
    print(d[n])
