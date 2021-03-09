import sys

input = sys.stdin.readline


def solution(n):
    memo = [4 for i in range(n + 1)]
    for i in range(1, n + 1):
        if i * i < n + 1:
            memo[i * i] = 1
        else:
            break

    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if memo[j] == 1:
                memo[i] = min(memo[i - j] + 1, memo[i])
    print(memo[n])


if __name__ == "__main__":
    solution(int(input().strip()))