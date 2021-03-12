from collections import deque
from bisect import bisect_left
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().strip().split()))
    count = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            count += 1
            b = i-1

    if count == 0:
        print(n)
    elif count > 1:
        print(0)
    else:
        answer = 0
        if b == 0 or (b > 0 and a[b-1] <= a[b+1]):
            answer += 1
        if (b < n-2 and a[b] <= a[b+2]) or b == n-2:
            answer += 1
        print(answer)
