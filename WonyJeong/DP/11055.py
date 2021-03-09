import sys

input = sys.stdin.readline


def solution(N, arr):
    dp = [val for val in arr]

    for i in range(N):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + arr[i])
        print(dp)
    print(max(dp))


if __name__ == "__main__":
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    solution(N, arr)
