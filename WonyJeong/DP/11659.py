import sys

input = sys.stdin.readline


def setMemo(arr):
    memo = [0]
    for i in range(0, len(arr)):
        memo.append(memo[i] + arr[i])
    return memo


if __name__ == "__main__":
    N, T = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    memo = setMemo(arr)
    for _ in range(T):
        s, e = map(int, input().strip().split())
        print(memo[e] - memo[s - 1])
