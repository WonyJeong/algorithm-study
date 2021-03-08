import sys

input = sys.stdin.readline


def solution(n, arr):
    if n < 3:
        answer = sum(arr)
    else:
        memo = [arr[0], arr[0] + arr[1], max(arr[0] + arr[2], arr[1] + arr[2])]
        for i in range(3, n):
            a = arr[i] + arr[i - 1] + memo[i - 3]
            b = arr[i] + memo[i - 2]
            memo.append(max(a, b))

        answer = memo[n - 1]
    return answer


if __name__ == "__main__":
    N = int(input().strip())
    arr = []
    for _ in range(N):
        arr.append(int(input().strip()))
    print(solution(N, arr))
