import sys

input = sys.stdin.readline


def solution(N, M, arr):
    l, r = 0, max(arr)

    while l <= r:
        mid = (l + r) // 2
        temp = sum([i - mid if mid < i else 0 for i in arr])
        if temp > M:
            l = mid + 1
        elif temp < M:
            r = mid - 1
        else:
            print(mid)
            return
    print(r)


if __name__ == "__main__":
    N, M = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    solution(N, M, arr)
