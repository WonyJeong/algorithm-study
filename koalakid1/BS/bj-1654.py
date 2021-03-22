from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    k, n = map(int, input().strip().split())
    length = [int(input()) for _ in range(k)]

    start, end = 1, max(length)
    while start <= end:
        mid = (start + end) // 2
        lines = 0
        for i in length:
            lines += i // mid

        if lines >= n:
            start = mid+1
        else:
            end = mid-1
    print(end)
