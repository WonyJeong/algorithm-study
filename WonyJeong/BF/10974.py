import sys
from itertools import permutations

input = sys.stdin.readline


def solution(N):
    for per in permutations(range(1, N + 1), N):
        print(" ".join(map(str, list(per))))


if __name__ == "__main__":
    N = int(input().strip())
    solution(N)
