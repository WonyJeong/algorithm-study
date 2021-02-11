import sys
from collections import deque

input = sys.stdin.readline


def move(start, to):
    answer.append([start, to])


def hanoi(N, start, to, via):
    if N == 1:
        move(start, to)
    else:
        hanoi(N - 1, start, via, to)
        move(start, to)
        hanoi(N - 1, via, to, start)


def solution(N):
    global answer
    answer = []
    hanoi(N, 1, 3, 2)
    return answer


if __name__ == "__main__":
    print(solution(3))