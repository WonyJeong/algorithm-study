import sys

input = sys.stdin.readline


def getYield(a, b, c):
    if c - b <= 0:
        return -1

    return a // (c - b) + 1


if __name__ == "__main__":
    answer = 0
    A, B, C = map(int, input().strip().split())
    print(getYield(A, B, C))
