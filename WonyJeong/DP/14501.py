import sys

input = sys.stdin.readline


def solution(n, arr):
    memo = [0 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        t, p = arr[i]
        if i + t <= n:
            memo[i] = max(memo[i + t] + p, memo[i + 1])
        else:
            memo[i] = memo[i + 1]
    print(memo[0])


if __name__ == "__main__":
    N = int(input().strip())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().strip().split())))
    solution(N, arr)
