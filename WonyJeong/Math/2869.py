import sys

input = sys.stdin.readline


def getDay(a, b, c):
    current = 0

    day = c // (a - b)

    print((c - b) % (a - b) == 0 and (c - b) // (a - b) or (c - b) // (a - b) + 1)


if __name__ == "__main__":
    answer = 0
    A, B, C = map(int, input().strip().split())
    getDay(A, B, C)
