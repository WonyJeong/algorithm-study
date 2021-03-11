import sys

input = sys.stdin.readline


def solution(N):
    answer = 0
    while N:
        answer += N % 2
        N = N // 2
    print(answer)


if __name__ == "__main__":
    solution(int(input().strip()))
