import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def solution(N, M, disable):
    arr = [i for i in range(10)]
    for i in disable:
        arr.remove(i)
    print(arr)


if __name__ == "__main__":
    N = int(input().strip())
    M = int(input().strip())
    disable = list(map(int, input().strip().split()))
    solution(N, M, disable)
