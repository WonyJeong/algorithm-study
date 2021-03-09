import sys
import math

input = sys.stdin.readline


def solution(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


if __name__ == "__main__":
    T = int(input().strip())
    for _ in range(T):
        r, n = map(int, input().strip().split())
        print(solution(n, r))
