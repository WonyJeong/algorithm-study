import sys
from collections import deque

input = sys.stdin.readline


def solution(n, money):
    answer = 0

    memo = [0 for _ in range(n + max(money))]

    for i in range(0, n):
        for j in money:
            memo[i + j] += 1

    print(memo)
    return answer


if __name__ == "__main__":
    print(solution(5, [1, 2, 5]))
