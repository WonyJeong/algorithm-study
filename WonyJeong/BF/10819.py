import sys
from itertools import permutations

input = sys.stdin.readline


def solution(N, arr):
    answer = 0
    for v in permutations(arr):
        vv = list(v)
        max_ = 0
        for i in range(0, len(vv) - 1):
            max_ += abs(vv[i] - vv[i + 1])
        if answer < max_:
            answer = max_

    print(answer)


if __name__ == "__main__":
    N = int(input().strip())
    solution(N, list(map(int, input().strip().split())))
